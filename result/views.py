from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db.models import Count
from . import models
from candidates.models import Csepresident,Csesecretory,Csevicepresident

# Votes stored in database
def csepresidentinput(request):
    if request.method=="POST":
          
            Cid=request.POST.get('voterInput')
            data = models.csepresidentres(cid=Cid)
            data.save()
            # print(Name,Usn,Password)
            return redirect('cse')
    return render(request,"cs.html")
      

def csevicepresidentinput(request):
    if request.method=="POST":
          
            Cid=request.POST.get('voterInput')
            data = models.csevicepresidentres(cid=Cid)
            data.save()
            # print(Name,Usn,Password)
            return redirect('cse')
    return render(request,"cs.html")

def csesecretoryinput(request):
    if request.method=="POST":
          
            Cid=request.POST.get('voterInput')
            data = models.csesecretoryres(cid=Cid)
            data.save()
            # print(Name,Usn,Password)
            return redirect('cse')
    return render(request,"cs.html")


# Result calculation 
def csepresidentresult(request):
  
  # Calling data pf candidates 
    csepresidentdata=Csepresident.objects.all()
    csevicepresidentdata=Csevicepresident.objects.all()
    csesecretorydata=Csesecretory.objects.all()

# Calling data of votes put for the candidates
    candidates = models.csepresidentres.objects.all()
    vicepresidentcandidates = models.csevicepresidentres.objects.all()
    vicesecretorycandidates = models.csesecretoryres.objects.all()


    vote_counts = {} #Dictionary to store vote count of president
    vote_counts1 = {} #Dictionary to store vote count of vicepresident
    vote_counts2 = {} #Dictionary to store vote count of secratory


# Calculating vote count of president
    for csepresident in csepresidentdata:
        # Filter candidates by the current Csepresident ID
        candidate_votes = candidates.filter(cid=csepresident.id)
        
        # Get the count of votes for this candidate
        vote_count = candidate_votes.aggregate(vote_count=Count('id'))['vote_count']

        vote_counts[vote_count] =  csepresident.id
        # print(f"Candidate ID: {csepresident.id}, Name: {csepresident.name}, Vote Count: {vote_count}")

# Calculating vote count of vice president
    for csevicepresident in csevicepresidentdata:
        # Filter candidates by the current Csepresident ID
        candidate_votes = vicepresidentcandidates.filter(cid=csevicepresident.id)
        
        # Get the count of votes for this candidate
        vote_count = candidate_votes.aggregate(vote_count=Count('id'))['vote_count']

        vote_counts1[vote_count] =  csevicepresident.id
        # print(f"Candidate ID: {csepresident.id}, Name: {csepresident.name}, Vote Count: {vote_count}")

# Calculating vote count of secratory
    for csevicesecratory in csesecretorydata:
        # Filter candidates by the current Csepresident ID
        candidate_votes = vicesecretorycandidates.filter(cid=csevicesecratory.id)
        
        # Get the count of votes for this candidate
        vote_count = candidate_votes.aggregate(vote_count=Count('id'))['vote_count']

        vote_counts2[vote_count] =  csevicesecratory.id
        # print(f"Candidate ID: {csepresident.id}, Name: {csepresident.name}, Vote Count: {vote_count}")

    data={
        'Csepresidentdata' : csepresidentdata,
        'Csevicepresidentdata' : csevicepresidentdata,
        'Csesecretorydata' : csesecretorydata,
        'Vote_counts_csepresident' : vote_counts,
        'Vote_counts_csevicepresident' : vote_counts1,
        'Vote_counts_csesecratory' : vote_counts2,
         }



    return render(request,"result.html",data)

