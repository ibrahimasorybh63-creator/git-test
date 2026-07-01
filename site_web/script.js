var nbr1,nbr2,op
const $ = document.getElementById.bind(document);
$('un').addEventListener('click',function(){
    $('resultat').value = $('resultat').value + "1"
});
$('deux').addEventListener('click',function(){
    $('resultat').value = $('resultat').value + "2"
});
$('trois').addEventListener('click',function(){
    $('resultat').value = $('resultat').value + "3"
});
$('quatre').addEventListener('click',function(){
    $('resultat').value = $('resultat').value + "4"
});
$('cinq').addEventListener('click',function(){
    $('resultat').value = $('resultat').value + "5"
});
$('six').addEventListener('click',function(){
    $('resultat').value = $('resultat').value + "6"
});
$('sept').addEventListener('click',function(){
    $('resultat').value = $('resultat').value + "7"
});
$('huit').addEventListener('click',function(){
    $('resultat').value = $('resultat').value + "8"
});
$('neuf').addEventListener('click',function(){
    $('resultat').value = $('resultat').value + "9"
});
$('zero').addEventListener('click',function(){
    $('resultat').value = $('resultat').value + "0"
});
$('addition').addEventListener('click',function(){
    nbr1 = $('resultat').value
    op="+"
    $('resultat').value = ""
});
$('soustraction').addEventListener('click',function(){
    nbr1 = $('resultat').value
    op="-"
    $('resultat').value = ""
});
$('multiplication').addEventListener('click',function(){
    nbr1 = $('resultat').value
    op="x"
    $('resultat').value = ""
});
$('division').addEventListener('click',function(){
    nbr1 = $('resultat').value
    op="/"
    $('resultat').value = ""
});
$('retour').addEventListener('click',function(){
    $('resultat').value = $('resultat').value.slice(0,-1)
});
$('modulo').addEventListener('click',function(){
    nbr1 = $('resultat').value
    op="mod"
    $('resultat').value = ""
});
$('factorielle').addEventListener('click',function(){
    nbr1 = parseInt($('resultat').value)
    let result = 1;
    for (let i=1;i<nbr1 +1;i++){
        result*= i
    }
    $('resultat').value = result
});
$('clear').addEventListener('click',function(){
    $('resultat').value = ""
});
$('expo').addEventListener('click',function(){
    $('resultat').value = $('resultat').value + "e+0"
    op = "exp"
});
$('virgule').addEventListener('click',function(){
    $('resultat').value = $('resultat').value + "."
});
$('e').addEventListener('click',function(){
    $('resultat').value = "2.7182818284590452353602874713527"
});
$('absolue').addEventListener('click',function(){
    if ($('resultat').value[0] == "-") {
        $('resultat').value = $('resultat').value.substring(1,$('resultat').value.length + 1)
    }
});
$('par2').addEventListener('click',function(){
    $('resultat').value = $('resultat').value + ")"
});
$('par1').addEventListener('click',function(){
    $('resultat').value = $('resultat').value + "("
});
$('inverse').addEventListener('click',function(){
    nbr1= $('resultat').value
    let result = 1/parseFloat(nbr1)
    $('resultat').value = result
});
$('negation').addEventListener('click',function(){
    if ($('resultat').value[0] == "-") {
        $('resultat').value = $('resultat').value.substring(1,$('resultat').value.length + 1)
    }
    else {
        $('resultat').value = "-" + $('resultat').value 
    }
});
$('ln').addEventListener('click',function(){
    nbr1 = parseFloat($('resultat').value)
    $('resultat').value = Math.log(nbr1)
});
$('log').addEventListener('click',function(){
    nbr1 = parseFloat($('resultat').value)
    $('resultat').value = Math.log10(nbr1)
});
$('puiss de dix').addEventListener('click',function(){
    nbr1 = parseFloat($('resultat').value)
    nbr1 = 10**nbr1
    $('resultat').value = nbr1
});
$('puissance').addEventListener('click',function(){
    nbr1 = $('resultat').value
    $('resultat').value = ""
});
$('racine carre').addEventListener('click',function(){
    nbr1 = parseFloat($('resultat').value)
    nbr1 = Math.sqrt(nbr1)
    $('resultat').value = nbr1
});
$('carre').addEventListener('click',function(){
    nbr1 = parseFloat($('resultat').value)
    nbr1 *= nbr1
    $('resultat').value = nbr1
});
$('pi').addEventListener('click',function(){
    $('resultat').value = "3.1415926535897932384626433832795"
});
$('egal').addEventListener('click',function(){
    nbr2 = $('resultat').value
    let result;
    switch(op) {
        case "+" :
            result = parseFloat(nbr1) + parseFloat(nbr2)
            $('resultat').value = result
            break;
        case "-" :
            result = parseFloat(nbr1) - parseFloat(nbr2)
            $('resultat').value = result
            break;
        case "x" :
            result = parseFloat(nbr1) * parseFloat(nbr2)
            $('resultat').value = result
            break;
        case "/" :
            result = parseFloat(nbr1) / parseFloat(nbr2)
            $('resultat').value = result
            break;
        case "mod":
            result = parseFloat(nbr1) % parseFloat(nbr2)
            $('resultat').value = result
            break;
        case "exp":
            result = parseFloat($('resultat').value)
            $('resultat').value = result
            break;
    }
});