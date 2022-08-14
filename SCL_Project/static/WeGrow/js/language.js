   function onLoad(){
   var l= localStorage.getItem("language");
   if(!l){
    localStorage.setItem("language","English")
    l="English"
   }
   var sel=document.getElementById("box1");
   if(l=="English")
    sel.selectedIndex=0;
   if(l=="Hindi")
   sel.selectedIndex=1;
   renderText(l);
  }
 function onSelectionFunction(sel) {
      localStorage.setItem("language",sel.options[sel.selectedIndex].text)
      renderText(sel.options[sel.selectedIndex].text)
    }
  function renderText(l){
    if(l==="English"){
    for(var i=0;i<20;i++){
      if(document.getElementById(i))
      document.getElementById(i).innerText=eng[i];
    }
  }
    else if(l==="Hindi")
    for(var i=0;i<20;i++){
    if(document.getElementById(i))
    document.getElementById(i).innerText=hin[i];
    }
  }