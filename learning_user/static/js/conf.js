angular
  .module("app", ["firebase"])
  .controller("appCtrl", function ($scope, $firebaseArray, $firebaseObject) {
    this.titre = "Angular Firebase CRUD";

    var ref = new Firebase("https://intense-fire-5995.firebaseio.com/ligues");
    this.ligues = $firebaseArray(ref);
    this.newLigue = { id: null, titre: "", code: "", sousTitre: "" };
    this.addLigue = function () {
      var ref3 = new Firebase(
        "https://intense-fire-5995.firebaseio.com/ligues/" + this.newLigue.code
      );
      var obj = $firebaseObject(ref3);
      obj.titre = this.newLigue.titre;
      obj.sousTitre = this.newLigue.sousTitre;
      obj.code = this.newLigue.code;
      obj.id = this.newLigue.id;
      obj.$save().then(
        function (ref) {
          console.log(obj.$id); // true
        },
        function (error) {
          console.log("Error:", error);
        }
      );
    };

    var ref2 = new Firebase("https://intense-fire-5995.firebaseio.com/ligues2");
    this.ligues2 = $firebaseArray(ref2);
  });
