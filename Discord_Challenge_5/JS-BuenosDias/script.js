  var dataHandler = document.getElementById("data");
  var lekHandler = document.getElementById("nazwaLeku");
  var liczbaHandler = document.getElementById("liczbaTabletek");
  var warunekHandler = document.getElementById("warunek");
  var dataInputHandler = document.getElementById("dateInput");

  var dni_tygodnia = new Array(7);
  dni_tygodnia[0] = "niedziela";
  dni_tygodnia[1] = "poniedziałek";
  dni_tygodnia[2] = "wtorek";
  dni_tygodnia[3] = "środa";
  dni_tygodnia[4] = "czwartek";
  dni_tygodnia[5] = "piątek";
  dni_tygodnia[6] = "sobota";

  var data = new Date();
  var dzien = data.getDate();
  var dzien_tygodnia = dni_tygodnia[data.getDay()];
  var miesiac = data.getMonth();
  var rok = data.getFullYear();

function wypiszIloscLeku(ile = 0){
  if(ile === 0){
    liczbaHandler.innerHTML = "Pora na spacer";
    return;
  }

  let wyraz;
  switch(ile){
    case 1: wyraz="tabletkę"; break;
    case 2:
    case 3:
    case 4: wyraz="tabletki"; break;
    default: wyraz="tabletek"; break;
  }

  liczbaHandler.innerHTML = `Weź ${ile} ${wyraz}.`;
}

function zmienDate(){
  let nowaData = dataInputHandler.value;
  let nowaDataArr = nowaData.split('-');
  if(nowaDataArr.length === 3){
    rok = nowaDataArr[0];
    miesiac = nowaDataArr[1];
    dzien = nowaDataArr[2];
    let nowyObjektDaty = new Date(rok, miesiac-1, dzien);
    dzien_tygodnia = dni_tygodnia[nowyObjektDaty.getDay()];
    main();
  }
}



function main(){
  miesiac = miesiac.toString();
  if(miesiac.length === 1) miesiac = `0${miesiac}`;
  var dzisJest = `Dziś jest ${dzien_tygodnia}, ${dzien}.${miesiac}.${rok}`;

  dataHandler.innerHTML = dzisJest;



  const alfabet = "aąbcćdeęfghijklłmnńoóprsśtuwyzźż";
  var suma = 0;

  for(const litera of dzien_tygodnia){
    suma += alfabet.indexOf(litera);
  }

  var srednia = suma/dzien_tygodnia.length;

  const leki = ["Hydrocodone", "Simvastatin", "Lisinopril", "Besylate", "Metformin", "Omeprazole", "Azithromycin"];

  var pierwszeLiteryLiczby = [];

  for(let lek of leki){
    lek = lek[0].toLowerCase();
    pierwszeLiteryLiczby.push(alfabet.indexOf(lek));
  }

  var indexNajblizej = 0;
  var odlegloscNajblizej = alfabet.length;

  for(let i=0; i<pierwszeLiteryLiczby.length; i++){
    let odleglosc = Math.abs(pierwszeLiteryLiczby[i]-srednia);
    if(odleglosc < odlegloscNajblizej){
    odlegloscNajblizej = odleglosc;
    indexNajblizej = i;
  }
  }

  lekHandler.innerHTML = `Weź lek o nazwie ${leki[indexNajblizej]}.`;

  var pierwZDnia = Math.sqrt(dzien);

  if(dzien % 10 == 0){
    warunekHandler.innerHTML = "Warunek podzielności."
    wypiszIloscLeku(0);
  }
  else if(Number.isInteger(pierwZDnia)){
    warunekHandler.innerHTML = "Warunek pierwiastka."
    wypiszIloscLeku(pierwZDnia);
  }
  else if(dzien > 15 && dzien < 31){
    warunekHandler.innerHTML = "Warunek przedziału."
    wypiszIloscLeku(2);
  }
  else{
    warunekHandler.innerHTML = "Brak spełnionego warunku."
    wypiszIloscLeku(1);
  }
}