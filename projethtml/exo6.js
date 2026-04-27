function ajouterunutilisateur(){ //creer une fonction
    //recuperer les id de html pour l'utilisateur
    const input=document.getElementById("utilisateur");
    const utilisateur=input.value
    const ajouterutilisateur=document.getElementById("ajouterutilisateur").value;
    const meessagerreur=document.getElementById("meessagerreur");
    //verifie les conditons 
    if (utilisateur.length ===0){ //si n'existe pas de l'utilisateur
        meessagerreur.style.display="block"
        return;
        }

    const elementcreer=document.createElement("li");
    elementcreer.textContent=utilisateur;
    document.getElementById('listutilisateur').appendChild(elementcreer);
    input.value='';
    
        listutilisateur.push(utilisateur[i].val)

    }

function ajouterunetache(){
    const input=document.getElementById("tache");
    const tache=input.value
    const ajoutertache=document.getElementById("ajoutertache");
    const erreurmessage=document.getElementById("erreurmessage");
    if (tache.length ===0){ //si n'existe pas de tache
        erreurmessage.style.display="block"
        }
     const elementcreer=document.createElement("li");
    elementcreer.textContent=tache;
    document.getElementById('listetache').appendChild(elementcreer);
    input.value='';

    //for(let i=0;i<tache.length;i++){
       // listetache.push(tache[i].val)//

    //}
    
}



