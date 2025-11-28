function rot13(str) 
{
  let arreglo = "";
  for(let i = 0; i < str.length; i++)
  {
    if(str.charCodeAt(i) >= 65 && str.charCodeAt(i) <= 90)
    {
      arreglo += String.fromCharCode((str.charCodeAt(i)+13-65)%26+65);
    }
    else
    {
      arreglo += String.fromCharCode(str.charCodeAt(i));
    }
  }
  return arreglo;
}


rot13("SERR PBQR PNZC");