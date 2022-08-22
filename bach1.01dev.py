#!/sw/bin/python2.2
import string, sys, pickle, cmd, random

class score_slice:
    def __init__(self):
       self.description=''
       self.number=0
       self.duration=0
       self.startingtime=0
       self.playinginstrument=""
       self.piece_of_score=[]
       
    def printscore(self):
       for line in self.piece_of_score:
           print line
           
    def compactify(self):
       output=""
       output+=";  -------------------------------------  \n"
       output+=";   Information about this piece of score \n"
       output+=";   Piece number  :"+str(self.number)   + "\n"
       output+=";   Description   : "+self.description   + "\n"
       output+=";   Instrument    : "+self.playinginstrument   + "\n"
       output+=";   Starting time : "+str(self.startingtime)   + "\n"
       output+=";   Duration      : "+str(self.duration) + "\n"
       output+=";                                         \n"
       for line in self.piece_of_score:
           output+=line
       return output
           
    def printall(self):
       print 20*"+"
       print "Information about this piece of score"
       print 'Piece number   :'+str(self.number)
       print 'Description    :'+str(self.description)
       print 'Instrument     :'+str(self.playinginstrument)
       print 'Starting time  :'+str(self.startingtime)
       print 'Duration       :'+str(self.duration)
       print 20*"+"
       for line in self.piece_of_score:
           print line
           
    def compactprint(self):
       output=""
       output+=";  -------------------------------------  \n"
       output+=";   Information about this piece of score \n"
       output+=";   Piece number  :"+str(self.number)   + "\n"
       output+=";   Description : "+self.description   + "\n"
       output+=";   Instrument    : "+self.playinginstrument   + "\n"
       output+=";   Starting time : "+str(self.startingtime)   + "\n"
       output+=";   Duration    : "+str(self.duration) + "\n"
       output+=";                                         \n"
       return output
           
          
class spartito(cmd.Cmd):

	def __init__(self):
		cmd.Cmd.__init__(self)
		self.prompt =  "BACH .:: "
		self.ftables='''
f1 0 4096 10 1                                  ; Simple sine
f2 0 4096 10 1 0 1 0 1 0.2 0.8 0.3 0.2          ; Clarinet-like
f3 0 2048  10 1 .5 .3 .25 .2 .167 .14 .125 .111 ; Sawtooth  
f4 0 2048  10 1 0  .3  0   .2  0  .14  0   .111 ; Square 
f5 0 2048  10 1 1 1 1 .7 .5 .3 .1               ; Pulse 
f6 0 2048  19 .5 1 270 1                        ; Granular parameters'''                               
		self.orchestra=[]
		self.docinstrument=[]
		self.score=[]
		self.header=''
		
	def help_randscore(self):
		print "Create a random score (specify the number of notes to be generated)"
	def do_randscore(self,score):
	  try:
	    if len(self.orchestra)==0:
	       print "BACH *** Warning empty orchestra"
	       print "          type <instrinit> to load the default orchestra"
	       print "          or use <instrimport> to import instruments from and external file\n"
	    n=0
	    while n<=0:
	      n=int(raw_input("Onsets to be generated : "))
	    strumento=0
	    while strumento <= 0: #or strumento>len(self.orchestra):
	      strumento=int(raw_input("Instrument : "))
	    choice=-1
	    if strumento==1:
	       
	       print 20*"-"
	       print "Select a waveform for the oscillator:\n"
	       print " [1] Simple sine"
	       print " [2] Clarinet-like"
	       print " [3] Sawtooth"
	       print " [4] Square"
	       print " [5] Pulse"
	       
	       while choice<=0 or choice>5:
	         choice=int(raw_input("Enter the waveform number (1-5): "))
	    if choice==-1:
	       choice=1
	         
	    tempo_inizio=-1
	    durata_min=-1
	    durata_max=-1
	    frequenza_min=-1
	    frequenza_max=-1
	    ampiezza=-1
	    while tempo_inizio<0:
	      tempo_inizio=float(raw_input("Start time (sec): "))
	    while durata_min<0:
	      durata_min=float(raw_input("Min duration (sec): "))
	    while durata_max<=0 or durata_max<durata_min:
	      durata_max=float(raw_input("Max duration (sec): "))
	    while frequenza_min<0:
	      frequenza_min=float(raw_input("Min frequency (Hz): "))
	    while frequenza_max<0 or frequenza_max<frequenza_min:
	      frequenza_max=float(raw_input("Max frequency (Hz): "))
	    while ampiezza<0 or ampiezza>20000:
	      ampiezza=float(raw_input("Amplitude (0-20000): "))
	    tempo=tempo_inizio
	    scorepiece=score_slice()
	    scorepiece.description='Random score'
	    
	    for i in range (1, n+1):
	        frequenza = random.random()*(frequenza_max-frequenza_min) + frequenza_min
	        durata = random.random()*(durata_max-durata_min) + durata_min
	        scoreline= "i"+str(strumento)+" "+str(tempo)+" "+str(durata)+" "+str(ampiezza)+" "+str(frequenza)+" "+str(choice)
	        #print scoreline
	        scoreline+="\n"
	        scorepiece.piece_of_score.append(scoreline)
	        tempo+=durata
	    scorepiece.duration=tempo
	    scorepiece.number=len(self.score)+1
	    scorepiece.startingtime=tempo_inizio
	    scorepiece.playinginstrument=str(strumento)
	    self.score.append(scorepiece)
	    print 39*"::"+"\n"
	    print scorepiece.compactify()
	    print 39*"::"+"\n"
	  except:
	    print "BACH *** Unexpected error occours"
	

	def help_randharmscore(self):
		print "Create a random score from the harmonic spectrum (specify the number of notes to be generated)"
	def do_randharmscore(self,score):
	  try:
	    if len(self.orchestra)==0:
	       print "BACH *** Warning empty orchestra"
	       print "          type <instrinit> to load the default orchestra"
	       print "          or use <instrimport> to import instruments from and external file\n"
	    n=0
	    while n<=0:
	      n=int(raw_input("Onsets to be generated : "))
	    strumento=0
	    while strumento <= 0: #or strumento>len(self.orchestra):
	      strumento=int(raw_input("Instrument : "))
	    choice=-1
	    if strumento==1:
	       
	       print 20*"-"
	       print "Select a waveform for the oscillator:\n"
	       print " [1] Simple sine"
	       print " [2] Clarinet-like"
	       print " [3] Sawtooth"
	       print " [4] Square"
	       print " [5] Pulse"
	       
	       while choice<=0 or choice>5:
	         choice=int(raw_input("Enter the waveform number (1-5): "))
	    if choice==-1:
	       choice=1
	         
	    tempo_inizio=-1
	    durata_min=-1
	    durata_max=-1
	    frequenza_min=-1
	    npartials=-1
	    ampiezza=-1
	    while tempo_inizio<0:
	      tempo_inizio=float(raw_input("Start time (sec): "))
	    while durata_min<0:
	      durata_min=float(raw_input("Min duration (sec): "))
	    while durata_max<=0 or durata_max<durata_min:
	      durata_max=float(raw_input("Max duration (sec): "))
	    while frequenza_min<0:
	      frequenza_min=float(raw_input("Base frequency (Hz): "))
	    while npartials<1 :
	      npartials=int(raw_input("Max number of partials (to set up the repository) : "))
	    while ampiezza<0 or ampiezza>20000:
	      ampiezza=float(raw_input("Amplitude (0-20000): "))
	    tempo=tempo_inizio
	    scorepiece=score_slice()
	    scorepiece.description='Random score with frequencies from the harmonic spectrum'
	    
	    for i in range (1, n+1):
	        frequenza = int(random.random()*int(npartials)+1)*frequenza_min
	        durata = random.random()*(durata_max-durata_min) + durata_min
	        scoreline= "i"+str(strumento)+" "+str(tempo)+" "+str(durata)+" "+str(ampiezza)+" "+str(frequenza)+" "+str(choice)
	        #print scoreline
	        scoreline+="\n"
	        scorepiece.piece_of_score.append(scoreline)
	        tempo+=durata
	    scorepiece.duration=tempo
	    scorepiece.number=len(self.score)+1
	    scorepiece.startingtime=tempo_inizio
	    scorepiece.playinginstrument=str(strumento)
	    self.score.append(scorepiece)
	    print 39*"::"+"\n"
	    print scorepiece.compactify()
	    print 39*"::"+"\n"
	  except:
	    print "BACH *** Unexpected error occours"



	def help_chaoscore(self):
		print "Create a score by means of the formula f_n=c*f_n-1 (1-f_n-1) (by specifing the number of notes to be generated)"
	def do_chaoscore(self,score):
	  #try:
	    if len(self.orchestra)==0:
	       print "BACH *** Warning empty orchestra"
	       print "          type <instrinit> to load the default orchestra"
	       print "          or use <instrimport> to import instruments from and external file\n"
	    n=0
	    while n<=0:
	      n=int(raw_input("Onsets to be generated : "))
	    strumento=0
	    while strumento <= 0: #or strumento>len(self.orchestra):
	      strumento=int(raw_input("Instrument : "))
	    choice=-1
	    if strumento==1:
	       
	       print 20*"-"
	       print "Select a waveform for the oscillator:\n"
	       print " [1] Simple sine"
	       print " [2] Clarinet-like"
	       print " [3] Sawtooth"
	       print " [4] Square"
	       print " [5] Pulse"
	       
	       while choice<=0 or choice>5:
	         choice=int(raw_input("Enter the waveform number (1-5): "))
	    if choice==-1:
	       choice=1
	         
	    tempo_inizio=-1
	    durata_min=-1
	    durata_max=-1
	    frequenza_min=-1
	    c=0
	    x_0=0
	    ampiezza=-1
	    while tempo_inizio<0:
	      tempo_inizio=float(raw_input("Start time (sec): "))
	    while durata_min<0:
	      durata_min=float(raw_input("Min duration (sec): "))
	    while durata_max<=0 or durata_max<durata_min:
	      durata_max=float(raw_input("Max duration (sec): "))
	    while frequenza_min<0:
	      frequenza_min=float(raw_input("Base frequency (Hz): "))
	    while x_0==0:
	      x_0=float(raw_input("Starting x value x_0 : "))
	    while c==0 :
	      c=float(raw_input("c coefficient in the formula f= c x (1-x) : "))
	    while ampiezza<0 or ampiezza>20000:
	      ampiezza=float(raw_input("Amplitude (0-20000): "))
	    tempo=tempo_inizio
	    scorepiece=score_slice()
	    scorepiece.description='Score with frequencies generated by means of the formula f=f0 * cx(1-x)'
	    
	    
	    for i in range (1, n+1):
	        x = float(c*x_0*(1-x_0))
	        durata = random.random()*(durata_max-durata_min) + durata_min
	        scoreline= "i"+str(strumento)+" "+str(tempo)+" "+str(durata)+" "+str(ampiezza)+" "+str(x*frequenza_min)+" "+str(choice)
	        #print scoreline
	        scoreline+="\n"
	        scorepiece.piece_of_score.append(scoreline)
	        tempo+=durata
	        x_0=x
	    scorepiece.duration=tempo
	    scorepiece.number=len(self.score)+1
	    scorepiece.startingtime=tempo_inizio
	    scorepiece.playinginstrument=str(strumento)
	    self.score.append(scorepiece)
	    print 39*"::"+"\n"
	    print scorepiece.compactify()
	    print 39*"::"+"\n"
	  #except:
	  #  print "BACH *** Unexpected error occours"




	def help_additiveinstr(self):
	   print "Create an instrument with additive synthesis giving information about the spectrum"
	
	def do_additiveinstr(self,instrname):
	   try:
	     n_of_partials=0
	     while n_of_partials<=0:
	         n_of_partials=raw_input("Number of partials ")
	     n_of_partials=int(n_of_partials)
	     spectrum="0"
	     print "Spectrum type:\n"
	     print "  [1] harmonic (f1:f2:f3: ... = 1:2:3: ...)"
	     print "  [2] ahharmonic - fixed detuning "
	     print "                   (f1:f2:f3: ... = 1:2*detuning:3*detuning: ...)"
	     print "  [3] anharmonic - random detuning "
	     print"                    (f1:f2:f3: ... = 1:2*random(0,1):3*random(0,1): ...)"
	     print "  [4] anharmonic - random frequency partials"
	     print "  [5] beats - random frequency beats"
	     while int(spectrum) not in range(1,6):
	         spectrum=raw_input("Enter code: ")
	     spectrum=int(spectrum)
	     
	     if spectrum==2:
	        detuning=0
	        while detuning==0:
	           detuning=float(raw_input("Detuning factor: "))
	        
	      
	     
	     spectralcomp="0"
	     print "Spectral components characterization"
	     print "  [1] amplitude of the partials decreasing like 1/n"
	     print "  [2] random amplitude "
	     print "  [3] constant amplitude"
	     print "  [4] linear decreasing amplitude"
	     while int(spectralcomp) not in range(1,5):
	         spectralcomp=raw_input("Enter code: ")
	     spectralcomp=int(spectralcomp)
	     if spectralcomp==4:
	        linearfactor=0
	        while linearfactor<=0:
	           linearfactor=float(raw_input("Decreasing factor: "))
	     envelyesno=""
	     while envelyesno=="" and spectralcomp==4:
	         envelyesno=raw_input("Add a linear envelope (y/n): ")
	     
	     try:
	        instrcounter=len(self.orchestra)
	        instrcounter+=1
	        instrbody=[]
	        
	        response=""
	        
	        while response=="":
	           response=raw_input("Would you like to save this instrument to an external file (y/n): ")

	        if len(self.header)>0 and (response=="y" or response=="Y"):
	           instrbody.append(self.header)
	        elif len(self.header)==0:
	           header="""
sr=44100 
kr=4410  
ksmps=10 
nchnls=2 
	         """
	           instrbody.append(self.header)
	        
	        instrbody.append("\t instr "+str(instrcounter)+"\n")
	        instrbody.append("kfond \t = \t p5 \n")
	        if envelyesno=="y" or envelyesno=="Y":
	            #stramplitude="kenv/"+str(n_of_partials)
	           stramplitude="kenv"
	        else:
	           stramplitude="p4"
	           
	        instrbody.append("kenv \t linen \t p4, 4, p3, 1\n")
	        instrbody.append("a1 \t oscili \t "+stramplitude+",p5,1 \n")
	        instrbody.append("krnd \t rand \t 1,-1 \n\n")
	        partial_amplitude=1
	        for partial in range (2,n_of_partials+1):
	            if str(spectrum)=="1":
	               line="k"+str(partial)+"freq \t = \t kfond*"+str(partial)+"\n"
	               instrbody.append(line)
	            if str(spectrum)=="2":
	               line="k"+str(partial)+"freq \t = \t kfond*"+str(partial)+"*"+str(detuning)+" \n"
	               instrbody.append(line)
	            if str(spectrum)=="3":
	                line="krnd"+str(partial)+" \t rand \t 1,-1 \n"
	                line+="k"+str(partial)+"freq \t = \t kfond*"+str(partial)+"*krnd"+str(partial)+" \n"
	                instrbody.append(line)
	            if str(spectrum)=="4":
	                line="krnd"+str(partial)+" \t rand \t kfond*"+str(partial)+",-1 \n"
	                line+="k"+str(partial)+"freq \t = \t kfond*"+str(partial)+"*krnd"+str(partial)+" \n"
	                instrbody.append(line)
	            if str(spectrum)=="5":
	                line="k"+str(partial)+"freq \t = \t kfond*"+str(random.random()*0.01+0.99)+" \n"
	                instrbody.append(line)
	                
	            line="a"+str(partial)+"partial \t oscili "+stramplitude+", k"+str(partial)+"freq,1 \n"
	            oldpartial_amplitude=partial_amplitude
	            if str(spectralcomp)=="1":
	               partial_amplitude=float(1/float(partial))
	            if str(spectralcomp)=="2":
	               partial_amplitude=random.random()
	            if str(spectralcomp)=="3":
	               partial_amplitude=float(1/float(n_of_partials))
	            if str(spectralcomp)=="4":
	               partial_amplitude=1-linearfactor*float(partial)
	               if partial_amplitude <=0:
	                  partial_amplitude=0
	            
	            line+="a"+str(partial)+" \t = a"+str(partial-1)+" + a"+str(partial)+"partial*"+str(partial_amplitude)+" \n"
	            instrbody.append(line)
	        instrbody.append("\n\n")
	        instrbody.append("outs a"+str(n_of_partials)+",a"+str(n_of_partials)+"\n")
	        instrbody.append("\t endin")
	        
	        lines=""
	        for instrline in instrbody:
	          lines+=instrline
	        self.orchestra.append(lines)
	        self.docinstrument.append("Instrument number "+str(instrcounter)+" generated via additive synthesis by BACH \n")
	        print "Instrument number "+str(instrcounter)+" generated via additive synthesis added to the orchestra"

	        if response=="y" or response=="Y":
	          while instrname=="":
	             instrname=raw_input("Instrument name (it will be created a .orc file with this name) ")
	          instrname=instrname+".orc"
	          saveFile=open(instrname,"w")
	          #if len(self.orchestra)==1:
	          #    saveFile.write(header+"\n\n")
	          #else:
	          #    saveFile.write("\n\n")
	          saveFile.write(header+"\n\n")
	          print instrname+" file opened for writing..."
	          print "Instrument characteristics"
	          print 4*" "+"Number of partials = "+str(n_of_partials)
	          for line in instrbody:
	             saveFile.write(line)
	          print "--> Done!"
	          saveFile.close()
	         
	         
	     except IOError, (errno,strerror):
	        print 'BACH *** I/O Problem occours... (%s): %s' % (errno,strerror)
	   except:
	      print "BACH *** Unexpected error occours..."


	def help_granularinstr(self):
	   print "Create a granular synthesis instrument"
	
	def do_granularinstr(self,instrname):
	   try:
	     amplitude=-1
	     pitch=-1
	     dens=-1
	     ampoff=-1
	     frqoff=-1
	     gdur=-1
	     gfn=-1
	     wfn=-1
	     mgdur=-1
	     
	     while amplitude<=0:
	         amplitude=int(raw_input("Aplitude: "))
	     
	     while pitch<=0:
	         pitch=int(raw_input("Pitch: "))
	     
	     while dens<=0:
	         dens=float(raw_input("Grain density: "))
	     
	     while ampoff<=0:
	         ampoff=float(raw_input("Aplitude offset: "))
	     
	     while frqoff<=0:
	         frqoff=float(raw_input("Frequency offset: "))
	     
	     while gdur<=0:
	         gdur=float(raw_input("Grain duration: "))
	     
	     while gfn<=0:
	         gfn=float(raw_input("Grain envelop function (have to be a power of two): "))
	     
	     while wfn<=0:
	         wfn=float(raw_input("Grain waveform function (have to be a power of two): "))
	     
	     while mgdur<=0:
	         mgdur=float(raw_input("Maximum grain duration: "))
	     
	     try:
	        instrcounter=len(self.orchestra)
	        instrcounter+=1
	        instrbody=[]
	        response=""
	        
	        while response=="":
	           response=raw_input("Would you like to save this instrument to an external file (y/n): ")

	        if len(self.header)>0 and (response=="y" or response=="Y"):
	           instrbody.append(self.header)
	        elif len(self.header)==0:
	           header="""
sr=44100 
kr=4410  
ksmps=10 
nchnls=2 
	         """
	           instrbody.append(self.header)
	        
	        instrbody.append("\t instr "+str(instrcounter)+"\n")
	        instrbody.append("iamp \t = \t"+ str (amplitude) +"\n")
	        instrbody.append("ipitch \t = \t"+ str (pitch) +"\n")
	        instrbody.append("idens \t = \t"+ str (dens) +"\n")
	        instrbody.append("iampoff \t = \t"+ str (ampoff) +"\n")
	        instrbody.append("ifrqoff \t = \t"+ str (frqoff) +"\n")
	        instrbody.append("igdur \t = \t"+ str (gdur) +"\n")
	        instrbody.append("igfn \t = \t"+ str (gfn) +"\n")
	        instrbody.append("iwfn \t = \t"+ str (wfn) +"\n")
	        instrbody.append("imgdur \t = \t"+ str (mgdur) +"\n")
	           
	        instrbody.append("a1 \t grain \t iamp,ipitch,idens,iampoff,ifrqoff,igdur,igfn,iwfn,imgdur \n")
	        instrbody.append("\n\n")
	        instrbody.append("outs a1,a1\n")
	        instrbody.append("\t endin")
	        
	        lines=""
	        for instrline in instrbody:
	          lines+=instrline
	        self.orchestra.append(lines)
	        self.docinstrument.append("Instrument number "+str(instrcounter)+" generated via granular synthesis by BACH \n")
	        print "Instrument number "+str(instrcounter)+" generated via granular synthesis added to the orchestra"
	        
	        response=""
	        
	        while response=="":
	           response=raw_input("Would you like to save this instrument to an external file (y/n): ")
	        if response=="y" or response=="Y":
	          while instrname=="":
	             instrname=raw_input("Instrument name (it will be created a .orc file with this name) ")
	          instrname=instrname+".orc"
	          saveFile=open(instrname,"w")
	          #if len(self.orchestra)==1:
	          #    saveFile.write(header+"\n\n")
	          #else:
	          #    saveFile.write("\n\n")
	          saveFile.write(header+"\n\n")
	          print instrname+" file opened for writing..."
	          for line in instrbody:
	             saveFile.write(line)
	          print "--> Done!"
	          print "WARNING!!! To actually use this orchestra file, the following line\n"
	          print "f2 0 4096 1 0.5 270 0.5\n"
	          print "have to be inserted in the score file"
	          saveFile.close()
	         
	         
	     except IOError, (errno,strerror):
	        print 'BACH *** I/O Problem occours... (%s): %s' % (errno,strerror)
	   except:
	      print "BACH *** Unexpected error occours..."
	   
	   

	def help_movescore(self):
	    print "Move a piece of score by providing the new starting time"
	def do_movescore(self,score):
	  #try:
	       piecenumber=-1
	       while piecenumber<0 or piecenumber>len(self.score):
	          piecenumber=raw_input("Enter the number of the piece of score to copy (use <shortprint>): ")
	          piecenumber=int(piecenumber)
	       selected_piece=self.score[piecenumber-1]

	       
	       #getting information from the original file to copy
	       scoreduration=selected_piece.duration
	       starting=selected_piece.startingtime
	       strumento=selected_piece.playinginstrument
	       
	       print "Starting time of the piece of score number "+str(piecenumber)+": "+str(starting)
	       print "Duration :"+str(scoreduration)+"\n"

	       newtime=float(-1)
	       while newtime<0:
	          newtime=float(raw_input("Enter starting time where you want to move: "))

	       splitline=[]
	       durstep=float(newtime)
	       counter=0
	       #oldstarting=float(float(starting)-durstep)
	       oldstarting=float(0)
	       
	       for scoreline in selected_piece.piece_of_score:
	           #print scoreline.split(' ')
	           splitline.append(scoreline.split(' '))
	           onsetstarting=splitline[counter][1]
	           onsetduration=float(splitline[counter][2])
	           #print 'onsetstarting= '+str(onsetstarting),
	           if str(onsetstarting) != '+':
	               onsetstarting=float(float(oldstarting)+float(durstep))
	               durstep=onsetduration
	               oldstarting=onsetstarting
	               #print 'changed to '+str(onsetstarting)
	           splitline[counter][2]=onsetduration
	           splitline[counter][1]=onsetstarting
	           counter=counter+1
	           
	       counter=0
	       for line in splitline:
	          newline=""
	          for lineelement in line:
	             newline=newline+str(lineelement)+" "
	             #print newline
	          newline=newline[:-1]
	          selected_piece.piece_of_score[counter]=newline
	          counter+=1
	       
	       selected_piece.startingtime=newtime
	       
	       print "The selected piece of score has been moved"
	       print selected_piece.compactify()
	  #except:
	  #   print "BACH *** Unexpected error occours..." 


	def help_copyscore(self):
	    print "Copy a piece of score and paste it by providing the starting time"
	def do_copyscore(self,score):
	  try:
	     if len(self.score)==0:
	        print "BACH *** Score empty"
	     else:
	       
	       piecenumber=-1
	       
	       while piecenumber<0 or piecenumber>len(self.score):
	          piecenumber=raw_input("Enter the number of the piece of score to copy (use <shortprint>): ")
	          piecenumber=int(piecenumber)
	       selected_piece=self.score[piecenumber-1]

	       
	       #getting information from the original file to copy
	       scoreduration=selected_piece.duration
	       starting=selected_piece.startingtime
	       strumento=selected_piece.playinginstrument
	       
	       print "Starting time of the piece of score number "+str(piecenumber)+": "+str(starting)
	       print "Duration :"+str(scoreduration)+"\n"

	       newtime=float(-1)
	       while newtime<0:
	          newtime=float(raw_input("Enter starting time where you want to paste the copy: "))

	       scorepiece=score_slice()
	       scorepiece.description='Copy of the piece score number '+str(piecenumber)

	       splitline=[]
	       durstep=float(newtime)
	       counter=0
	       #oldstarting=float(float(starting)-durstep)
	       oldstarting=float(0)
	       
	       for scoreline in selected_piece.piece_of_score:
	           #print scoreline.split(' ')
	           splitline.append(scoreline.split(' '))
	           onsetstarting=splitline[counter][1]
	           onsetduration=float(splitline[counter][2])
	           #print 'onsetstarting= '+str(onsetstarting),
	           if str(onsetstarting) != '+':
	               onsetstarting=float(float(oldstarting)+float(durstep))
	               durstep=onsetduration
	               oldstarting=onsetstarting
	               #print 'changed to '+str(onsetstarting)
	           splitline[counter][2]=onsetduration
	           splitline[counter][1]=onsetstarting
	           counter=counter+1
	           
	       counter=0
	       for line in splitline:
	          newline=""
	          for lineelement in line:
	             newline=newline+str(lineelement)+" "
	             #print newline
	          newline=newline[:-1]
	          scorepiece.piece_of_score.append(newline)
	          counter+=1
	       
	       scorepiece.duration=scoreduration
	       scorepiece.number=len(self.score)+1
	       scorepiece.startingtime=newtime
	       scorepiece.playinginstrument=str(strumento)
	       self.score.append(scorepiece)
	       print "The selected piece of score has been copyed"
	       print 39*"::"+"\n"
	       print scorepiece.compactify()
	       print 39*"::"+"\n"
	       
	  except:
	     print "BACH *** Unexpected error occours..." 

    


	def help_insertscore(self):
	    print "Edit and insert a piece of score by providing all the information"
	def do_insertscore(self,score):
	  try:
	     if len(self.score)==0:
	        print "BACH *** Score empty"
	     else:
	       
	       piecenumber=-1
	       
	       while piecenumber<0 or piecenumber>len(self.score):
	          piecenumber=raw_input("Enter the number of the piece of score to copy (use <shortprint>): ")
	          piecenumber=int(piecenumber)
	       selected_piece=self.score[piecenumber-1]

	       
	       #getting information from the original file to copy
	       scoreduration=selected_piece.duration
	       starting=selected_piece.startingtime
	       strumento=selected_piece.playinginstrument
	       
	       print "Starting time of the piece of score number "+str(piecenumber)+": "+str(starting)
	       print "Duration :"+str(scoreduration)+"\n"

	       newtime=float(-1)
	       while newtime<0:
	          newtime=float(raw_input("Enter starting time where you want to paste the copy: "))

	       scorepiece=score_slice()
	       scorepiece.description='Copy of the piece score number '+str(piecenumber)

	       splitline=[]
	       durstep=float(newtime)
	       counter=0
	       #oldstarting=float(float(starting)-durstep)
	       oldstarting=float(0)
	       
	       for scoreline in selected_piece.piece_of_score:
	           #print scoreline.split(' ')
	           splitline.append(scoreline.split(' '))
	           onsetstarting=splitline[counter][1]
	           onsetduration=float(splitline[counter][2])
	           #print 'onsetstarting= '+str(onsetstarting),
	           if str(onsetstarting) != '+':
	               onsetstarting=float(float(oldstarting)+float(durstep))
	               durstep=onsetduration
	               oldstarting=onsetstarting
	               #print 'changed to '+str(onsetstarting)
	           splitline[counter][2]=onsetduration
	           splitline[counter][1]=onsetstarting
	           counter=counter+1
	           
	       counter=0
	       for line in splitline:
	          newline=""
	          for lineelement in line:
	             newline=newline+str(lineelement)+" "
	             #print newline
	          newline=newline[:-1]
	          scorepiece.piece_of_score.append(newline)
	          counter+=1
	       
	       scorepiece.duration=scoreduration
	       scorepiece.number=len(self.score)+1
	       scorepiece.startingtime=newtime
	       scorepiece.playinginstrument=str(strumento)
	       self.score.append(scorepiece)
	       print "The selected piece of score has been copyed"
	       print 39*"::"+"\n"
	       print scorepiece.compactify()
	       print 39*"::"+"\n"
	       
	  except:
	     print "BACH *** Unexpected error occours..." 



	def help_expandscore(self):
	    print "Copy a piece of score and paste it expanded by providing the expansion factor and the starting time"
	def do_expandscore(self,score):
	  try:
	     if len(self.score)==0:
	        print "BACH *** Score empty"
	     else:
	       
	       piecenumber=-1
	       
	       while piecenumber<0 or piecenumber>len(self.score):
	          piecenumber=raw_input("Enter the number of the piece of score to expand (use <shortprint>): ")
	          piecenumber=int(piecenumber)
	       selected_piece=self.score[piecenumber-1]

	       
	       #getting information from the original file to copy
	       scoreduration=selected_piece.duration
	       starting=selected_piece.startingtime
	       strumento=selected_piece.playinginstrument
	       
	       #print "Starting time of the piece of score number "+str(piecenumber)+": "+str(starting)
	       print "Duration :"+str(scoreduration)+"\n"

	       expansion=float(-1)
	       while expansion<0:
	          expansion=float(raw_input("Enter expansion time factor: "))

	       splitline=[]
	       durationarray=[]
	       counter=0
	       total_duration=0
	       for scoreline in selected_piece.piece_of_score:
	           #print scoreline.split(' ')
	           splitline.append(scoreline.split(' '))
	           onsetduration=float(splitline[counter][2])*expansion
	           splitline[counter][2]=onsetduration
	           if counter>=1:
	              splitline[counter][1]=float(splitline[counter-1][1])+float(splitline[counter-1][2])
	           total_duration+=onsetduration
	           counter+=1
	           
	       counter=0
	       for line in splitline:
	          newline=""
	          for lineelement in line:
	             newline=newline+str(lineelement)+" "
	             #print newline
	          newline=newline[:-1]
	          selected_piece.piece_of_score[counter]=newline
	          counter+=1

	       selected_piece.description="Score "+str(piecenumber)+ " expanded by a factor "+str(expansion)
	       
	       selected_piece.duration=total_duration
	       print "The selected piece of score has been modified"
	       print 39*"::"+"\n"
	       print selected_piece.compactify()
	       print 39*"::"+"\n"
	       
	  except:
	     print "BACH *** Unexpected error occours..." 


	def help_changeinstr(self):
	    print "Change the playing instrument of a piece of score"
	def do_changeinstr(self,score):
	  try:
	     if len(self.score)==0 or len(self.orchestra)==0:
	        print "BACH *** Score empty or no instruments loaded in memory"
	     else:
	       
	       piecenumber=-1
	       
	       while piecenumber<0 or piecenumber>len(self.score):
	          piecenumber=raw_input("Enter the number of the piece of score (use <shortprint>): ")
	          piecenumber=int(piecenumber)
	       selected_piece=self.score[piecenumber-1]

	       
	       #getting information from the original file to copy
	       scoreduration=selected_piece.duration
	       starting=selected_piece.startingtime
	       strumento=selected_piece.playinginstrument
	       try:
	          docinstr=self.docinstrument[int(strumento)]
	          print "Playing instrument "+str(strumento)+" : "+docinstr
	       except:
	          print "BACH *** Warning: the selected score does not have a playing instrument belonging to the current orchestra"
	       
	       #print "Starting time of the piece of score number "+str(piecenumber)+": "+str(starting)
	       print "Duration :"+str(scoreduration)+"\n"
	       print "\n Instruments in the orchestra actually in memory (1-"+str(len(self.orchestra))+"): "
	       instrnum=1
	       for doc in self.docinstrument:
	          print "Instrument "+str(instrnum)+": ",string.ljust(doc,40)
	          instrnum+=1

	       newinstrument=float(-1)
	       while newinstrument<0 or newinstrument>len(self.orchestra):
	          newinstrument=int(raw_input("Enter new instrument number: "))

	       splitline=[]
	       counter=0
	       for scoreline in selected_piece.piece_of_score:
	           #print scoreline.split(' ')
	           splitline.append(scoreline.split(' '))
	           #oldinstrument=float(splitline[counter][0])
	           #oldinstrument=oldinstriment[1:]
	           splitline[counter][0]="i"+str(newinstrument)
	           counter+=1
	           
	       counter=0
	       for line in splitline:
	          newline=""
	          for lineelement in line:
	             newline=newline+str(lineelement)+" "
	             #print newline
	          newline=newline[:-1]
	          selected_piece.piece_of_score[counter]=newline
	          counter+=1

	       selected_piece.description=selected_piece.description+" - instrument changed"
	       selected_piece.playinginstrument=str(newinstrument)
	       print "The selected piece of score has been modified"
	       print 39*"::"+"\n"
	       print selected_piece.compactify()
	       print 39*"::"+"\n"
	       
	  except:
	     print "BACH *** Unexpected error occours..." 


	def help_changeamp(self):
	    print "Change the amplitude of a piece of score"
	def do_changeamp(self,score):
	  try:
	     if len(self.score)==0 or len(self.orchestra)==0:
	        print "BACH *** Score empty or no instruments loaded in memory"
	     else:
	       
	       piecenumber=-1
	       
	       while piecenumber<0 or piecenumber>len(self.score):
	          piecenumber=raw_input("Enter the number of the piece of score (use <shortprint>): ")
	          piecenumber=int(piecenumber)
	       selected_piece=self.score[piecenumber-1]

	       
	       #getting information from the original file to copy
	       scoreduration=selected_piece.duration
	       starting=selected_piece.startingtime
	       print "Duration :"+str(scoreduration)+"\n"
	       
	       newampl=float(-1)
	       while newampl<0 or newampl>20000:
	          newampl=int(raw_input("Enter new amplitude (0-20000): "))

	       splitline=[]
	       counter=0
	       for scoreline in selected_piece.piece_of_score:
	           #print scoreline.split(' ')
	           splitline.append(scoreline.split(' '))
	           splitline[counter][3]=str(newampl)
	           counter+=1
	           
	       counter=0
	       for line in splitline:
	          newline=""
	          for lineelement in line:
	             newline=newline+str(lineelement)+" "
	             #print newline
	          newline=newline[:-1]
	          selected_piece.piece_of_score[counter]=newline
	          counter+=1

	       selected_piece.description=selected_piece.description+" - amplitude changed"
	       print "The selected piece of score has been modified"
	       print 39*"::"+"\n"
	       print selected_piece.compactify()
	       print 39*"::"+"\n"
	       
	  except:
	     print "BACH *** Unexpected error occours..." 


	def help_changewaveform(self):
	    print "Change the waveform (the f-table number) for an oscillator (instrument 1) playing a piece of score"
	def do_changewaveform(self,score):
	  try:
	     if len(self.score)==0 or len(self.orchestra)==0:
	        print "BACH *** Score empty or no instruments loaded in memory"
	     else:
	       
	       piecenumber=-1
	       
	       while piecenumber<0 or piecenumber>len(self.score):
	          piecenumber=raw_input("Enter the number of the piece of score (use <shortprint>): ")
	          piecenumber=int(piecenumber)
	       selected_piece=self.score[piecenumber-1]

	       
	       #getting information from the original file to copy
	       scoreduration=selected_piece.duration
	       starting=selected_piece.startingtime
	       print "Duration :"+str(scoreduration)+"\n"
	       print "Available waveforms:"
	       print "[1] Simple sine"
	       print "[2] Clarinet-like"
	       print "[3] Sawtooth"
	       print "[4] Square"
	       print "[5] Pulse"
	       
	       newwf=float(-1)
	       while newwf<=0 or newwf>5:
	          newwf=int(raw_input("Enter new waveform: "))

	       splitline=[]
	       counter=0
	       for scoreline in selected_piece.piece_of_score:
	           #print scoreline.split(' ')
	           splitline.append(scoreline.split(' '))
	           splitline[counter][5]=str(newwf)
	           counter+=1
	           
	       counter=0
	       for line in splitline:
	          newline=""
	          for lineelement in line:
	             newline=newline+str(lineelement)+" "
	             #print newline
	          newline=newline[:-1]
	          newline+="\n"
	          selected_piece.piece_of_score[counter]=newline
	          counter+=1

	       selected_piece.description=selected_piece.description+" - waveform changed"
	       print "The selected piece of score has been modified"
	       print 39*"::"+"\n"
	       print selected_piece.compactify()
	       print 39*"::"+"\n"
	       
	  except:
	     print "BACH *** Unexpected error occours..." 



	def help_deletescore(self):
	    print "Delete a piece of score"
	def do_deletescore(self,score):
	  try:
	     if len(self.score)==0:
	        print "BACH *** Score empty"
	     else:
	       
	       piecenumber=-1
	       
	       while piecenumber<0 or piecenumber>len(self.score):
	          piecenumber=raw_input("Enter the number of the piece of score to delete (use <shortprint>): ")
	          piecenumber=int(piecenumber)
	       selected_piece=self.score[piecenumber-1]

	       
	       #getting information from the original file to copy
	       scoredescription=selected_piece.description
	       starting=selected_piece.startingtime
	       strumento=selected_piece.playinginstrument
	       
	       #print "Starting time of the piece of score number "+str(piecenumber)+": "+str(starting)
	       print "Piece to delete Information \n"
	       print "                Number      :"+str(piecenumber)
	       print "                Description :"+str(scoredescription)
	       print "                Instrument  :"+str(strumento)

	       confirmation=""
	       while confirmation!="y" and confirmation!="Y" and confirmation!="n" and confirmation!="N":
	          confirmation=raw_input("Confirm deletion (y/n): ")
	       
	       if confirmation=="y" or confirmation=="Y":
	          try:
	              del self.score[piecenumber-1]
	              print "The selected piece of score has been deleted"
	          except:
	              print "BACH *** Error during delete process"
	       
	  except:
	     print "BACH *** Unexpected error occours..." 



	def help_revertscore(self):
	    print "Revert a selected piece of score"
	def do_revertscore(self,score):
	  try:
	     if len(self.score)==0:
	        print "BACH *** Score empty"
	     else:
	       
	       piecenumber=-1
	       
	       while piecenumber<0 or piecenumber>len(self.score):
	          piecenumber=raw_input("Enter the number of the piece of score to revert (use <shortprint>): ")
	          piecenumber=int(piecenumber)
	       selected_piece=self.score[piecenumber-1]

	       	       
	       splitline=[]
	       swaparray=[] 
	       durationarray=[]
	       counter=0
	       total_duration=0
	       number_of_onsets=len(selected_piece.piece_of_score)
	       print "Number of onsets to revert: "+str(number_of_onsets)

	       #fill the scoreline array
	       for scoreline in selected_piece.piece_of_score:
	           splitline.append(scoreline.split(' '))
	           #create a copy of the array
	           swaparray.append(scoreline.split(' '))
	           
	       #revert the score    
	       for counter in range(0,number_of_onsets):
	           new_onsetduration=float(swaparray[number_of_onsets-counter-1][2])
	           new_onsetamplitude=float(swaparray[number_of_onsets-counter-1][3])
	           new_onsetfrequency=float(swaparray[number_of_onsets-counter-1][4])
	           splitline[counter][2]=new_onsetduration
	           splitline[counter][3]=new_onsetamplitude
	           splitline[counter][4]=new_onsetfrequency
	           counter+=1


	       counter=0
	       for line in splitline:
	          newline=""
	          for lineelement in line:
	             newline=newline+str(lineelement)+" "
	             #print newline
	          newline=newline[:-1]
	          selected_piece.piece_of_score[counter]=newline
	          counter+=1

	       selected_piece.description="Score "+str(piecenumber)+ " reverted"
	       
	       print "The selected piece of score has been modified"
	       print 39*"::"+"\n"
	       print selected_piece.compactify()
	       print 39*"::"+"\n"
	       
	  except:
	     print "BACH *** Unexpected error occours..." 

	def help_mirrorscore(self):
	    print "Starting from a piece of score it creates a new one sharing the score in two parts and using the first one, reverted, as second part"
	def do_mirrorscore(self,score):
	  try:
	     if len(self.score)==0:
	        print "BACH *** Score empty"
	     else:
	       
	       piecenumber=-1
	       
	       while piecenumber<0 or piecenumber>len(self.score):
	          piecenumber=raw_input("Enter the number of the piece of score to revert (use <shortprint>): ")
	          piecenumber=int(piecenumber)
	       selected_piece=self.score[piecenumber-1]

	       	       
	       splitline=[]
	       durationarray=[]
	       counter=0
	       total_duration=0
	       number_of_onsets=len(selected_piece.piece_of_score)
	       print "Number of onsets to revert: "+str(number_of_onsets)

	       #fill the scoreline array
	       for scoreline in selected_piece.piece_of_score:
	           splitline.append(scoreline.split(' '))
	           
	       #revert the score    
	       for counter in range(int(number_of_onsets/2),number_of_onsets):
	           new_onsetduration=float(splitline[number_of_onsets-counter-1][2])
	           new_onsetamplitude=float(splitline[number_of_onsets-counter-1][3])
	           new_onsetfrequency=float(splitline[number_of_onsets-counter-1][4])
	           splitline[counter][2]=new_onsetduration
	           splitline[counter][3]=new_onsetamplitude
	           splitline[counter][4]=new_onsetfrequency
	           counter+=1


	       counter=0
	       for line in splitline:
	          newline=""
	          for lineelement in line:
	             newline=newline+str(lineelement)+" "
	             #print newline
	          newline=newline[:-1]
	          selected_piece.piece_of_score[counter]=newline
	          counter+=1

	       selected_piece.description="Score "+str(piecenumber)+ " mirrored"
	       
	       print "The selected piece of score has been modified"
	       print 39*"::"+"\n"
	       print selected_piece.compactify()
	       print 39*"::"+"\n"
	       
	  except:
	     print "BACH *** Unexpected error occours..." 



	def help_complementscore(self):
	    print "Modify a score by complementing the note frequencies with a value fixed by the user"
	def do_complementscore(self,score):
	  try:
	     if len(self.score)==0:
	        print "BACH *** Score empty"
	     else:
	       
	       piecenumber=-1
	       
	       while piecenumber<0 or piecenumber>len(self.score):
	          piecenumber=raw_input("Enter the number of the piece of score to modify (use <shortprint>): ")
	          piecenumber=int(piecenumber)
	       selected_piece=self.score[piecenumber-1]

	       complement=float(-1)
	       while complement<0:
	          complement=float(raw_input("Enter complement frequency: "))

	       splitline=[]
	       durationarray=[]
	       counter=0
	       total_duration=0
	       number_of_onsets=len(selected_piece.piece_of_score)

	       #fill the scoreline array
	       for scoreline in selected_piece.piece_of_score:
	           splitline.append(scoreline.split(' '))
	           
	       for counter in range(0,number_of_onsets):
	           new_onsetfrequency=float(complement-float(splitline[counter][4]))
	           splitline[counter][4]=new_onsetfrequency
	           counter+=1


	       counter=0
	       for line in splitline:
	          newline=""
	          for lineelement in line:
	             newline=newline+str(lineelement)+" "
	             #print newline
	          newline=newline[:-1]
	          selected_piece.piece_of_score[counter]=newline
	          counter+=1
	       selected_piece.description="Score "+str(piecenumber)+ " complemented at "+str(complement)
	       
	       print "The selected piece of score has been modified"
	       print 39*"::"+"\n"
	       print selected_piece.compactify()
	       print 39*"::"+"\n"
	       
	  except:
	     print "BACH *** Unexpected error occours..." 

	def help_transposescore(self):
	    print "Modify a score by transposition"
	def do_transposescore(self,score):
	  try:
	     if len(self.score)==0:
	        print "BACH *** Score empty"
	     else:
	       
	       piecenumber=-1
	       
	       while piecenumber<0 or piecenumber>len(self.score):
	          piecenumber=raw_input("Enter the number of the piece of score to modify (use <shortprint>): ")
	          piecenumber=int(piecenumber)
	       selected_piece=self.score[piecenumber-1]
	       print "Select a transposition :"
	       print "[1] by providing an additive factor      (new_freq=old_freq + shift_factor)"
	       print "[2] by providing a multiplicative factor (new_freq=old_freq * shift_factor)"
	       print "    (Es. to traspose of a fifth, select [2] and enter 1.5 as shift_factor)"
	       
	       
	       choice=-1
	       
	       while choice<=0 or choice>2:
	          choice=int(raw_input("Enter your choice: "))

	       shift_factor=float(0)
	       while shift_factor==0:
	          shift_factor=float(raw_input("Enter shift factor: "))

	       splitline=[]
	       durationarray=[]
	       counter=0
	       total_duration=0
	       number_of_onsets=len(selected_piece.piece_of_score)

	       #fill the scoreline array
	       for scoreline in selected_piece.piece_of_score:
	           splitline.append(scoreline.split(' '))
	           
	       for counter in range(0,number_of_onsets):
	           if choice==1:
	              new_onsetfrequency=float(float(splitline[counter][4])+shift_factor)
	           else:
	              new_onsetfrequency=float(float(splitline[counter][4])*shift_factor)
	           
	           splitline[counter][4]=new_onsetfrequency
	           counter+=1


	       counter=0
	       for line in splitline:
	          newline=""
	          for lineelement in line:
	             newline=newline+str(lineelement)+" "
	             #print newline
	          newline=newline[:-1]
	          selected_piece.piece_of_score[counter]=newline
	          counter+=1
	       selected_piece.description="Score "+str(piecenumber)+ " transposed"
	       
	       print "The selected piece of score has been modified"
	       print 39*"::"+"\n"
	       print selected_piece.compactify()
	       print 39*"::"+"\n"
	       
	  except:
	     print "BACH *** Unexpected error occours..." 



	def help_insert(self):
		print"Insert a row in the score"
	def do_insert(self, name):
	  try:
	    while name=="":
	       name=raw_input("Raw to be inserted in the score : ")
	       
	    scoreline=name
	    scoreline+="\n"
	    
	    scorepiece=score_slice()
	    scorepiece.description='Score line inserted manually'
	    scorepiece.piece_of_score.append(scoreline)
	    self.score.append(scorepiece)
	    print 39*"::"+"\n"
	    print scorepiece.compactify()
	    print 39*"::"+"\n"
		#print ""
	    #print "Raw: " + name + " Added to the score"
	  except:
	    print "BACH *** Unexpected error occours"
	    		
	def help_print(self):
		print "Print the generated score"
	def do_print(self,line):
		print 60*"="
		print "Score generated by BACH\n\n"	
		print self.ftables
		for score_line in self.score:
		      score_line.printall()
		print ""	
		print 60*"="

	def help_shortprint(self):
		print "Print the generated score"
	def do_shortprint(self,line):
		print 60*"="
		print "Score generated by BACH\n\n"	
		print self.ftables
		for score_line in self.score:
		      print score_line.compactprint()
		print ""	
		print 60*"="
	       
	def help_viewheader(self):
	    print "Display the orchestra header"
	def do_viewheader(self,score):
	    print 78*"="
	    print "Orchestra Header:\n"
	    print self.header
	    print 78*"="
	       
	def help_setheader(self):
	    print "Set the CSound Orchestra Header"
	def do_setheader(self,score):
	    try:
	       sr=0
	       kr=0
	       nchnls=0
	       while sr==0:
	         sr=int(raw_input("sr = (negative values turns to default value: 44100) "))
	       if sr<0:
	          sr=int(44100)
	          print "sr set to 44100 by default"
	       while kr==0 or kr>sr:
	         kr=int(raw_input("kr = (negative values turns to default value: 4410) "))
	       if kr<0:
	          kr=int(4410)
	          print "kr set to 4410 by default"
	       ksmps=int(sr/kr)
	       print "ksmps = "+str(ksmps)
	       while nchnls<=0 or nchnls>8:
	         nchnls=int(raw_input("nchnls = "))
	       self.header="\t sr="+str(sr)+"\n"
	       self.header+="\t kr="+str(kr)+"\n"
	       self.header+="\t ksmps="+str(ksmps)+"\n"
	       self.header+="\t nchnls="+str(nchnls)+"\n"
	       print "\n Header: \n"
	       print self.header
	    except:
	       print 'BACH *** Unexpected problem occours...'
	    
	def help_instrinit(self):
	    print "Loads default instruments set"
	def do_instrinit(self,score):
	    if self.header=="":
	       self.header="""
	         sr=44100 
	         kr=4410  
	         ksmps=10 
	         nchnls=2 
	     
	       """
	    print "Loading default instruments sets... \n"
	    
	    # Loading instruments and docs
	    strumento1="""
	       instr 1
	    a1 oscil  p4,p5,p6
	       outs a1,a1 
	       endin
	       
	    """
	    docstrumento1="Simple Sin oscillator (1 harmonic or foundamental, no other partials)"

	    strumento2="""
	         instr 2   
	    kenv linen  p4, 4, p3, 1  
	    a2   oscil  kenv/3,p5,2 
	    a3   oscil  kenv/3,p5*1.003,2
	    a4   oscil  kenv/3,p5*0.997,2
	    atot  =  a2+a3+a4
 	    
	         outs   atot, atot    
	         endin
	     
	    """
	    docstrumento2="Complex three oscillator system with beats"
	    
	    strumento3="""
	         instr 3 
	    kenv linen  1, p3*.75, 1, p3*0.25 
	    a1   pluck  p4, p5, p5, 0, 1
	         outs   a1,a1
	         endin 
	     
	    """
	    docstrumento3="Karplus-strong Pluck Instrument"
	    
	    strumento4="""
	          instr 4         
	    iamp    =  p4    
	    ipitch  =  p5  
	    idens   =  30   
	    iampoff =  10000 
	    ifrqoff =  200 
	    igdur   =   0.05 
	    istereo =  0.5   
	    igfn    =  1   
	    iwfn    =  2   
	    imgdur  =  .5   
	    a1     grain  iamp,ipitch,idens,iampoff,ifrqoff,igdur,igfn,iwfn,imgdur 
	           outs   a1*istereo,a1*(1-istereo)    
	           endin    
	    
	    """
	    docstrumento4="Granular synthesis instrument"
	    
	    strumento5="""
	           instr 5

  	  ifreq		=	p5
	  iamp		=	p4/2 ; amplitude, scaled for two sources
	  afilt		init	0
	  ifeed		=	1
	  ieccdur		=	0.01
	  icutoff		=	8000
	  aecc		linseg 1,ieccdur,0,p3-ieccdur,0
	  asum		=	aecc+afilt*ifeed
	  adel		delay	asum,1/ifreq
	  afilt		tone	adel,icutoff
	  aout		atone afilt*iamp,30
      index        = 6.0             ; modulation index
      ipan         = 0.5  
      ifmamp       = .7              ; % of total amp, 1=dB amp as in p4
      ifmrise      = .2 * p3         ; % of total dur, 1=entire dur of note
      ifmdec       = .7 * p3         ; % of total duration
      ifmoff       = p3 - (ifmrise + ifmdec)

   
      kfm          linseg    0, ifmrise, ifmamp, ifmdec, 0, ifmoff, 0
      kndx         =         kfm * index
      afm1         foscil    iamp, ifreq, 1, 7, kndx, 1
      afm2         foscil    iamp, ifreq * 1.003, 1.003, 2.003, kndx, 1
      afm          =         kfm * (afm1+afm2)
      aMixSig         = (aout+afm)

      ;--stereo panning around 90 degrees
      iCirclePan      = 90.0 * ipan         ; scale 90 with values from 0 to 1
      kdegree         line      iCirclePan, p3, iCirclePan
      kdistance       line      1, p3, 1    ; used to distance reverb, need a constant 1
      asig1, asig2    locsig    aMixSig, kdegree, kdistance, 0.0
      outs            asig1, asig2
	
      endin

      """

	    #self.orchestra.append(header)
	    docstrumento5="Karplus-Strong pluck plus FM - Stereo panning aroung 90 degrees"
	    
	    if len(self.orchestra) == 0:
	       self.orchestra.append(strumento1)
	       self.docinstrument.append(docstrumento1)
	       self.orchestra.append(strumento2)
	       self.docinstrument.append(docstrumento2)
	       self.orchestra.append(strumento3)
	       self.docinstrument.append(docstrumento3)
	       self.orchestra.append(strumento4)
	       self.docinstrument.append(docstrumento4)
	       self.orchestra.append(strumento5)
	       self.docinstrument.append(docstrumento5)
	       print 78*"="
	       for instrument in self.docinstrument:
	           print "+ "+instrument + " --> Loaded in memory"
	       print 78*"="
	    else:
	       print "WARNING: BACH orchestra is not empty: instrinit failed. Try <clearorc> first to clear the orchestra\n Nothing done" 


	def help_csexport(self):
	    print "Save the current score"
	def do_csexport(self,filename):
	    while filename=="":
	       filename=raw_input("Enter score file name (.sco automatically added): ")
	    scorename = filename + ".sco"
	    orcname   = filename + ".orc"
	    try:
	       scoFile=open(scorename,"w")
	       #print "Writing score file ..."
	       scoFile.write(self.ftables)
	       scoFile.write("\n\n")
	       for scorepiece in self.score:
	           scoFile.write(scorepiece.compactify())
	           scoFile.write("\n")
	       scoFile.close()
	       print 78*"="
	       print ".::. Score file: " + scorename + " saved on disk"
 	    except IOError, (errno,strerror):
	       print 'BACH *** I/O Problem occours while writing score file... (%s): %s' % (errno,strerror)

	    try:
	       orcFile=open(orcname,"w")
	       #print "Writing orchestra file ..."
	       if len(self.header)==0:
	          header="""
sr=44100 
kr=4410  
ksmps=10 
nchnls=2 
	         """
	          
	       orcFile.write(self.header)
	       orcFile.write("\n")
	       for strumento,documentazione in zip(self.orchestra,self.docinstrument):
	           orcFile.write(";***BACH "+documentazione)
	           orcFile.write(strumento)
	           orcFile.write("\n")
	       orcFile.close()
	       print ".::. Orchestra file: "+orcname+" generated automatically and saved on disk"
	       print 78*"="
 	    except IOError, (errno,strerror):
	       print 'BACH *** I/O Problem occours while writing orchestra file ... (%s): %s' % (errno,strerror)





	def help_instrimport(self):
	    print "Import instruments from an (external) orchestra file"
	def do_instrimport(self,score):
	    filename=""
	    while filename=="":
	      filename=str(raw_input("External Orchestra file to be imported: "))
	    try:
	      print 78*"="
	      print "Opening "+filename+" ..."
	      lines=open(filename).readlines()
	      #for line in lines:
	      #  print line
	      #print 60*"="
	      line=lines[0]
	      linecounter=0
	      instrcounter=len(self.orchestra)
	      startingnumber=instrcounter
	      while linecounter<len(lines):
	         line=lines[linecounter]
	         pos=string.find(line,"instr")
	         if pos >=0 :
	           try:
	            instrcounter+=1
	            linecounter+=1
	            print "Instrument founded in orchestra "+filename+" and added to BACH as instrumen number "+str(instrcounter)
	            strumento="\t instr "+str(instrcounter)+"\n"
	            while linecounter<len(lines) and string.find(lines[linecounter],"endin")<0:
	               strumento+=lines[linecounter]
	               linecounter+=1
	            strumento+="\t endin\n"
	            #print 78*"#"
	            #print strumento
	            #print 78*"#"
	            self.orchestra.append(strumento)
	            self.docinstrument.append("Instrument number "+str(instrcounter)+" imported from "+filename+"\n")
	           except:
	             print "BACH *** Loop error"
	         linecounter+=1
	      print "...done!\n"
	      print str(instrcounter-startingnumber)+" instrument(s) imported to the BACH orchestra \n"
	      print 78*"="
	    except IOError, (errno,strerror):
	      print 'BACH *** I/O Problem occours while opening external orchestra file ... (%s): %s' % (errno,strerror)
	      
	      
	    
	def help_glissa(self):
	    print "Create a score piece using a glissando bewteen two frequencies, with a certain stepping value"
	def do_glissa(self,score):
	  try:
	    if len(self.orchestra)==0:
	       print "BACH *** Warning empty orchestra"
	       print "          type <instrinit> to load the default orchestra"
	       print "          or use <instrimport> to import instruments from and external file\n"
	    
	    strumento=-1
	    while strumento <= 0: #or strumento>len(self.orchestra):
	       strumento=int(raw_input("Instrument number: "))
	    choice=-1
	    if strumento==1:
	       print 20*"-"
	       print "Select a waveform for the oscillator:\n"
	       print " [1] Simple sine"
	       print " [2] Clarinet-like"
	       print " [3] Sawtooth"
	       print " [4] Square"
	       print " [5] Pulse"
	       while choice<=0 or choice>5:
	          choice=int(raw_input("Enter the waveform number (1-5): "))
	    if choice==-1:
	       choice=1
	    
	    tempo_inizio=-1
	    while tempo_inizio<0:
	       tempo_inizio=float(raw_input("Starting time (sec): "))
	    frequenza_inizio=-1
	    while frequenza_inizio<0:
	       frequenza_inizio=float(raw_input("Starting frequency (Hz): "))
	    frequenza_fine=-1
	    while frequenza_fine<0:
	       frequenza_fine=float(raw_input("Ending frequency (Hz): "))
	    step=-1
	    while step<=0 or step >= abs(frequenza_fine-frequenza_inizio):
	       step=float(raw_input("Step (Hz): "))
	    if frequenza_fine<frequenza_inizio:
	       step=step*(-1)
	    durata_nota=-1
	    while durata_nota<0:
	       durata_nota=float(raw_input("Onset duration (sec): ")) 
	    ampiezza=-1
	    while ampiezza<0 or ampiezza>20000:
	       ampiezza=int(raw_input("Amplitude (0-20000): "))
	    
	    tempo=tempo_inizio
	    scorepiece=score_slice()
	    scorepiece.description='Glissando'

	    line="i" + str(strumento) + " " + str(tempo_inizio)+ " " + str(durata_nota) + " "+str(ampiezza)+" " + str(frequenza_inizio) + " " + str(choice)
	    #print line
	    scoreline=line
	    scoreline+="\n"
	    scorepiece.piece_of_score.append(scoreline)
	    tempo+=durata_nota
	    
	    for frequenza in range(frequenza_inizio+step,frequenza_fine+step,step):
	        scoreline="i"+str(strumento)+" + " + str(durata_nota) + " "+str(ampiezza)+" "+ str(frequenza) + " " + str(choice)
	        scoreline+="\n"
	        scorepiece.piece_of_score.append(scoreline)
	        tempo+=durata_nota
	    scorepiece.duration=tempo
	    scorepiece.number=len(self.score)+1
	    scorepiece.startingtime=tempo_inizio
	    scorepiece.playinginstrument=str(strumento)
	    self.score.append(scorepiece)
	    print 39*"::"+"\n"
	    print scorepiece.compactify()
	    print 39*"::"+"\n"

	  except:
	     print "BACH *** Problems occour while executing glissa ..."

	def help_brownscore(self):
	    print "Create a score piece using a brownian motion bewteen two frequencies, with a certain stepping value"
	def do_brownscore(self,score):
	  try:
	    if len(self.orchestra)==0:
	       print "BACH *** Warning empty orchestra"
	       print "          type <instrinit> to load the default orchestra"
	       print "          or use <instrimport> to import instruments from and external file"
	    
	    strumento=-1
	    while strumento <= 0: #or strumento>len(self.orchestra):
	       strumento=int(raw_input("Instrument number: "))
	    choice=-1
	    if strumento==1:
	       print 20*"-"
	       print "Select a waveform for the oscillator:\n"
	       print " [1] Simple sine"
	       print " [2] Clarinet-like"
	       print " [3] Sawtooth"
	       print " [4] Square"
	       print " [5] Pulse"
	       while choice<=0 or choice>5:
	          choice=int(raw_input("Enter the waveform number (1-5): "))
	    if choice==-1:
	       choice=1
	    
	    n=-1
	    while n<0:
	       n=float(raw_input("Number of onsets to be generated: "))
	    tempo_inizio=-1
	    while tempo_inizio<0:
	       tempo_inizio=float(raw_input("Starting time (sec): "))
	    overlapping=-1
	    while overlapping<0:
	       overlapping=float(raw_input("Overlapping time (sec): "))
	    startingfreq=-1
	    while startingfreq<0:
	       startingfreq=float(raw_input("Starting frequency (Hz): "))
	    lowerbound=-1
	    while lowerbound<0:
	       lowerbound=float(raw_input("Lower bound frequency (Hz): "))
	    higherbound=-1
	    while higherbound<0 or higherbound<lowerbound:
	       higherbound=float(raw_input("Higher bound frequency (Hz): "))
	    stepfreq=-1
	    while stepfreq<=0 or stepfreq >= (higherbound-lowerbound):
	       stepfreq=float(raw_input("Step (Hz): "))
	    minduration=-1
	    while minduration<0:
	       minduration=float(raw_input("Minimum Onset Duration (sec): "))
	    maxduration=-1
	    while maxduration<0 or maxduration<minduration:
	       maxduration=float(raw_input("Maximum Onset Duration(sec): "))
	    amp=-2
	    while amp<-1 or amp>20000:
	       amp=float(raw_input("Amplitude (0-20000, or -1 to have a random value): "))
	    frequency=startingfreq
	    time=tempo_inizio
	    scorepiece=score_slice()
	    scorepiece.description='Brownian Score'
	    counter=0
	    while counter < n:
	      control=random.random()
	      if control<.5:
	        if frequency > (lowerbound + stepfreq):
	           frequency = frequency - stepfreq
	        else:
	           frequency=lowerbound
	      else:
	        if frequency < (higherbound - stepfreq):
	           frequency = frequency + stepfreq
	        else:
	           frequency=higherbound
	      if amp == -1:
	         amp=random.random()*10000+10000
	      overlap=random.random()*overlapping
	      event_time=time-overlap
	      if event_time < 0:
	         event_time=time
	      pan=random.random()
	      pluckamp=random.random()
	      pluckdur=random.random()
	      duration=random.random()*maxduration+minduration
	      
	      scoreline = "i"+str(strumento)+" "+str(event_time) + " " + str(duration) + " " + str(amp) + " " +str(frequency)+ " " + str(choice)
	      scoreline+="\n"
	      scorepiece.piece_of_score.append(scoreline)
	      time+=duration
	      counter+=1
	    scorepiece.duration=time
	    scorepiece.number=len(self.score)+1
	    scorepiece.startingtime=tempo_inizio
	    scorepiece.playinginstrument=str(strumento)
	    self.score.append(scorepiece)
	    print 39*"::"+"\n"
	    print scorepiece.compactify()
	    print 39*"::"+"\n"

	  except:
	    print "BACH *** Problems occour while executing brownscore ..."

			
	def	help_quit(self):
		print "Quit the program"
	def do_quit(self,line):
	    aaa=raw_input("Really Exit (y/n): ")
	    if aaa=="y" or aaa=="Y":
	      print "Exiting from BACH..."
	      sys.exit()
	      
	def	help_clearscore(self):
		print "Reset the score generated deleting all the onsets. The whole score will be lost"
	def do_clearscore(self,line):
	    aaa=raw_input("Really clear the score (y/n): ")
	    if aaa=="y" or aaa=="Y":
	       self.ftables='''
		               f1 0 4096 10 1                                   ; Simple Sine
		               f2 0 4096 10 1 0 1 0 1 0.2 0.8 0.3 0.2           ; Clarinet-like        
                       f3  0 2048  10 1 .5 .3 .25 .2 .167 .14 .125 .111 ; Sawtooth  
                       f4  0 2048  10 1 0  .3  0   .2  0  .14  0   .111 ; Square 
                       f5  0 2048  10 1 1 1 1 .7 .5 .3 .1               ; Pulse 
                       f6  0 2048  19 .5 1 270 1                        ; Granular parameters'''           
            self.score=[]                    
	      
	def	help_clearorc(self):
		print "Delete all the instruments actually in the orchestra"
	def do_clearorc(self,line):
	    aaa=raw_input("Really delete all the instruments (y/n): ")
	    if aaa=="y" or aaa=="Y":
	       self.orchestra=[]
	       self.docinstrument=[]
	       self.header=""
	      


	def help_instrview(self):
	    print "Displays details concerning an instrument. Usage: instrview <instrument number>"
	def do_instrview(self, instrnum):
	    try:
	       while int(instrnum<=0) or instrnum=="":
	          instrnum=int(raw_input("Instrument number: "))
	    except:
	       print "BACH*** Input error occurs ..."
	       
	    try:
	       if self.orchestra[int(instrnum)-1]=="" or int(instrnum)>len(self.orchestra):
	          print "Sorry, Instrument "+str(instrnum)+ "does not exist in the current orchestra"
	       else:
	          print "\n Instrument "+str(instrnum)+": " + self.docinstrument[int(instrnum)-1] + "\n"
	          print self.orchestra[int(instrnum)-1]
	    except:
	       print "BACH*** Orchestra error occurs ..."
	       
	       
    
	def	help_about(self):
	   print "About BACH ... "
	def do_about(self,score):
	   print "\n\n"
	   print "***                                                      ***"
	   print "*** Welcome to BACH (Basic Algorithmic Composition Help) ***"
	   print "***                 Version 1.0a                         ***"
	   print "***  (c) 2003 Domenico Vicinanza and Vittorio Cafagna    ***"
	   print "***       DMI - University of Salerno (Italy)            ***"
	   print "***                                                      ***"
	   print "\n"
	   
	def help_instrlist(self):
	    print "Print the CSound Instrument List"
	def do_instrlist(self,score):
	    if len(self.docinstrument) == 0:
	       print """
Sorry, no instrument loaded.
   type <instrinit> to load the default instruments set
   or   <instrimport> to load an instruments set from an external .orc file               
	    
	             """
	    else:
	        instrnum=1
	        print 78*"="
	        for doc in self.docinstrument:
	           print "Instrument "+str(instrnum)+": ",string.ljust(doc,40)
	           instrnum+=1
	           print "\n"
	        print 78*"="
   	
	
if __name__ == "__main__":
    print "\n\n"
    print "***                                                      ***"
    print "*** Welcome to BACH (Basic Algorithmic Composition Help) ***"
    print "***                 Version 1.0a                         ***"
    print "***  (c) 2003 Domenico Vicinanza and Vittorio Cafagna    ***"
    print "***       DMI - University of Salerno (Italy)            ***"
    print "***                                                      ***"
    print "\n"
    print "       .:: Type help to have the command list ::."
    print "\n\n"
    
    
    
    brano=spartito()
    brano.cmdloop()		
		