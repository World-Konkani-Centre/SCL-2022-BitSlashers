 function onLoad(){
    var l= localStorage.getItem("language");
    if(!l){
     localStorage.setItem("language","English")
     l="English"
    }
    var sel=document.getElementById("box1");
    if(l=="English")
     sel.selectedIndex=0;
    if(l=="Kannada")
    sel.selectedIndex=1;
    if(l=="Konkani")
    sel.selectedIndex=2;
    renderText(l);
   }
  function onSelectionFunction(sel) {
       localStorage.setItem("language",sel.options[sel.selectedIndex].text)
       renderText(sel.options[sel.selectedIndex].text)
     }
   function renderText(l){
     if(l==="English"){
     for(var i=0;i<10000;i++){
       if(document.getElementById(i))
       document.getElementById(i).innerText=eng[i];
     }
   }
     else if(l==="Kannada")
     for(var i=0;i<10000;i++){
     if(document.getElementById(i))
     document.getElementById(i).innerText=kan[i];
     }
     else if(l==="Konkani")
     for(var i=0;i<10000;i++){
     if(document.getElementById(i))
     document.getElementById(i).innerText=konkani[i];
     }
   }