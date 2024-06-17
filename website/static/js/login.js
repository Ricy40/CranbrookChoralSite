
function yummers() {
    var passphrase = document.getElementById("passphrase").value;
    if (passphrase === "1234") {
        console.log("Correct passphrase");
        document.getElementById("LogIn").style.display = "none";
        document.getElementById("LoggedIn").style.display = "block";
    }
}