var synth = window.speechSynthesis;
    var utterance = new SpeechSynthesisUtterance();

    function speak(text) {
        var text = document.getElementById(text).textContent;
        utterance.text = text;
        synth.speak(utterance);
        isSpeaking=true;
    }
    function stop()
    {
        synth.cancel();
        isSpeaking=false;
    }
    document.getElementById("speakButton").addEventListener("click",function(){
        if(isSpeaking){
            stop();
        }else{
            speak();
        }
    })
    document.getElementById("speakButton").addEventListener("dblclick",
    function(event){
            event.stopPropagation();
            speak();
        });
        
        