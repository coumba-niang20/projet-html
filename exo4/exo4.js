
 function ajouterunlement(){
    const element =document.getElementById("element");
    const valeurelement=element.value;
    if (valeurelement !==''){
            const elementcreer=document.createElement("li");
            elementcreer.textContent=valeurelement;
            document.getElementById('listedynamique').appendChild(elementcreer);
            element.value='';
        }

    

}