function palindrome(str) 
{
  let min = str.toLowerCase();
  min = min.replace(/[^0-9a-z]/gi, '') 

  let reversa = min.split('').reverse().join('');
  
  if( min == reversa)
  {
    return true;
  }
  else
  {
    return false;
  }
  
}

palindrome("2A3*3a2");