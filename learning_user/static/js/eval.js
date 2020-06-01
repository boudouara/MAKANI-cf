$(document).ready(function() {
	$('.js-menu').on('click', function(e) {
		e.preventDefault();
	//display menu nav-icon
		$(this).toggleClass('is-open');
	//show slide bar
		$('.slide-bar').toggleClass('is-open');
	//body stop overflow
		$("body").toggleClass("overflow-hidden");
		$(".overlay").toggleClass("is-active");
	});
	
	$('.overlay').on('click', function(e) {
		e.preventDefault();
		$('.nav-icon').removeClass('is-open');
		$('.slide-bar').removeClass('is-open');
		$('.subnav-list').removeClass('is-display');
		$(".nav-link-icon").removeClass('is-open');
		$("body").removeClass("overflow-hidden");
		$(".overlay").removeClass("is-active");
	});
	
	//display nav-list__items
	$('.js-nav').on('click', function(e) {
		e.preventDefault();
		$(this).find('.subnav-list').toggleClass('is-display');
		$(".nav-link-icon").toggleClass('is-open');
	});
});
// Dès le départ, on initialise une liste des élèves :
// On créé un objet listeEleves avec des propriétés et méthodes:
var listeEleves = {
  eleves: [], // C'est la liste des élèves

  // L'objet listeEleves a une fonction exprès pour gérer l'affichage
  afficher: function () {
    // D'abord on supprime l'ensemble des élèves :
    $("#liste-eleves").html("");

    if (this.eleves.length == 0) {
      $("#liste-eleves").html("Aucun evaluateur dans la liste !");
      return true;
    }
    // ensuite, pour chaque élève, on créé le <li> qui va bien
    this.eleves.forEach(function (eleve, index) {
      // on créé le li
      var li = $("<li>").addClass("list-group-item");
      var idEleve = "eleve-" + eleve.id;
      // On donne l'identifiant au LI
      li.attr("id", idEleve);
      // on créé la description de l'élève
      var description = $("<strong>").html(
        eleve.civilite + " " + eleve.prenom + " " + eleve.nom + " " + eleve.specialite
      );
      // on créé la div qui contient les boutons
      var divBoutons = $("<div>").addClass("pull-right links");
      // on créé le lien editer et supprimer
      var lienEditer = $("<a>")
        .addClass("btn btn-sm btn-primary")
        .html('<i class="fa fa-edit"></i> Editer')
        .click(function () {
          switchTitle("editer");
          listeEleves.modifier(eleve.id);
        });
      var lienSupprimer = $("<a>")
        .addClass("btn btn-sm btn-danger")
        .html('<i class="fa fa-times"></i> Supprimer')
        .click(function () {
          listeEleves.supprimer(eleve.id);
        });
      // on créé le clearfix
      var clearfix = $("<div>").addClass("clearfix");
      // On place les liens dans la divBoutons
      divBoutons.append(lienEditer, " ", lienSupprimer);
      // On ajoute dans le li la description, les boutons et le clearfix
      li.append(description, divBoutons, clearfix);
      // Maintenant que notre li est prêt, on ajoute le li dans la liste des élèves
      $("#liste-eleves").append(li);
    });
  },

  // L'objet listeEleves a une fonction qui permet facilement d'ajouter un élève dans le tableau
  ajouter: function (eleve) {
    // D'abord on vérifie si l'élève a un id :
    if (eleve.id == "") {
      eleve.id = this.eleves.length;
    }

    // On ajoute l'élève dans le tableau
    this.eleves.push(eleve);
    // On demande le raffraichissement de la liste
    this.afficher();
  },

  // L'objet listeEleve a une fonction qui permet de trouver un eleve avec
  // son identifiant
  trouver: function (id) {
    // L'élève qu'on voudra retourner
    var eleveATrouver = false;
    // pour chaque eleve du tableau
    this.eleves.forEach(function (eleve) {
      console.log(id, eleve.id);
      // si l'élève a le même id que celui demandé, cela signifie qu'on a trouvé
      if (eleve.id == id) {
        // donc on renvoie cet élève !
        eleveATrouver = eleve;
      }
    });
    return eleveATrouver;
  },

  // L'objet listeEleve a une fonction qui permet de supprimer un élève
  supprimer: function (id) {
    // Pour chaque élève du tableau
    for (var i = 0; i < this.eleves.length; i++) {
      // si un élève a le même id que celui demandé
      if (this.eleves[i].id == id) {
        // on supprime l'élément i du tableau
        this.eleves.splice(i, 1);
      }
    }
    this.afficher();
  },

  mettreAJour: function (eleve) {
    for (var i = 0; i < this.eleves.length; i++) {
      if (this.eleves[i].id == eleve.id) {
        this.eleves[i] = eleve;
      }
    }

    this.afficher();
  },

  modifier: function (id) {
    var eleve = this.trouver(id);
    console.log(id, eleve);
    if (!eleve) {
      alert("Une erreur est survenue, nous ne trouvons pas l'élève " + id);
      return false;
    }
    $("#id").val(eleve.id);
    $("#nom").val(eleve.nom);
    $("#prenom").val(eleve.prenom);
    $("#civilite").val(eleve.civilite);

    $("#section-eleve").show();
  }
};

// Quand le document est pleinement chargé :
$(document).ready(function () {
  // On charge les élèves existant via Ajax :
  $.get(
    "http://www.json-generator.com/api/json/get/ceJsIUFdLm?indent=2",
    function (data) {
      // Quand on a récupérer la liste, on la met en place dans notre
      // objet listeEleves
      listeEleves.eleves = data;
      // Ensuite on demande à l'objet listeEleves de les afficher
      listeEleves.afficher();
    }
  );
  // On branche les actions sur les boutons :
  // Quand on clique sur le bouton ajouter, le formulaire
  // doit apparaitre
  $("#bouton-ajouter").click(function () {
    clearForm(); // On nettoie le formulaire
    switchTitle("ajouter"); // On met en place le bon titre
    $("#section-eleve").show(); // on montre le formulaire
  });

  // Quand le formulaire est soumis par l'utilisateur, on
  // examine et on enregistre
  $("#formulaire-eleve").submit(function (e) {
    e.preventDefault(); // On empêche la véritable action de soumission
    // On récupère les valeurs du formulaire :
    var nomEleve = $("#nom").val();
    var prenomEleve = $("#prenom").val();
    var civiliteEleve = $("#civilite").val();
    var idEleve = $("#id").val();
    // On créé l'objet élève
    var eleve = {
      nom: nomEleve,
      prenom: prenomEleve,
      civilite: civiliteEleve,
      id: idEleve
    };

    // Si l'élève avait un identifiant, c'est qu'il n'est pas
    // nouveau, donc on remplace plutôt que d'ajouter
    if (eleve.id != "") {
      listeEleves.mettreAJour(eleve);
    } else {
      // On ajoute l'élève au tableau des élèves
      listeEleves.ajouter(eleve);
    }
    clearForm();
  });

  $("#bouton-fermer").click(function () {
    clearForm();
  });
});

// fonctions utilitaires :

// Permet de nettoyer le formulaire et de le fermer
function clearForm() {
  $("#section-eleve").hide();
  $("#nom").val("");
  $("#id").val("");
  $("#prenom").val("");
}

function switchTitle(action) {
  $("#titre-editer, #titre-ajouter").hide();

  if (action == "editer") {
    $("#titre-editer").show();
  } else {
    $("#titre-ajouter").show();
  }
}
