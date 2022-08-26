 function onLoad(){
    var l= localStorage.getItem("language");
    if(!l){
     localStorage.setItem("language","English")
     l="English"
    }
    var sel=document.getElementById("language-selector");
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
     for(var i=0;i<100;i++){
       if(document.getElementById(i))
       document.getElementById(i).innerText=eng[i];
     }
     if(document.getElementById("video1")){
     if(document.getElementById("video2"))document.getElementById("video2").remove();
      var parent = document.getElementById('video1');
      var customElement = createCustomElement("https://youtu.be/cfTRou4JtW8","glightbox play-btn video2");
      parent.appendChild(customElement);
      console.log(document.getElementById("video2"))
     }
      return;
   }
     else if(l==="Kannada"){
     for(var i=0;i<100;i++){
     if(document.getElementById(i))
     document.getElementById(i).innerText=kan[i];
     }
     if(document.getElementById("video1")){
      if(document.getElementById("video2"))document.getElementById("video2").remove();
      var parent = document.getElementById('video1');
      var customElement = createCustomElement("https://youtu.be/LIvm_GfcTWo","glightbox play-btn");
      parent.appendChild(customElement);
      return;
     }
     }
     else if(l==="Konkani"){
     for(var i=0;i<100;i++){
     if(document.getElementById(i))
     document.getElementById(i).innerText=konkani[i];
     }
     if(document.getElementById("video1")){
      if(document.getElementById("video2"))document.getElementById("video2").remove();
      var parent = document.getElementById('video1');
      var customElement = createCustomElement("https://youtu.be/S7GDda309JU","glightbox play-btn");
      parent.appendChild(customElement);
      return;
     }
     } 
   }
   function createCustomElement( anchorLink,anchorClass){
    var aTag = document.createElement("a");
    aTag.href = anchorLink;
    const myArray = anchorClass.split(" ");
    for(var i=0;i<2;i++){
    aTag.classList.add(myArray[i]);
    }
    aTag.setAttribute("id","video2")
    return aTag ;
  }