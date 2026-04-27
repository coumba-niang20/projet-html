function envoyeformulaire(){

    const formulaire=document.querySelector("form")
    const nom=document.getElementById('nom').value
    const age=document.getElementById("age").value
    const sexe=document.querySelector('input[name="sexe"]:checked')
    const loisirs=document.querySelectorAll('input[name="loisirs"]:checked')
    const pays=document.getElementById("pays").value
    const commentaire=document.getElementById("commentaire").value
    const erreurmessage=document.getElementById("erreurmessage")
    if (loisirs.length ===0){
        erreurmessage.style.display="block"
    }
    let listloisirs=[]
    for (let i =0;i<loisirs.length;i++){
        listloisirs.push(loisirs[i].value)
    
    }
    let donnees={
        nom:nom,
        age:age,
        sexe:sexe.value,
        loisirs:listloisirs,
        pays:pays,
        commentaire:commentaire
    }
    alert(JSON.stringify(donnees,null,2))
    console.log(donnees)


}