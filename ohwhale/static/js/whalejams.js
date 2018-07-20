//var whalejams = (function() {
	
	// Initilize Wavesurfer

	// Grab all wave-surfer containers
	var waveForms = document.getElementsByClassName('waveform');

	// Loop through each and pass to createSurfer
	for (i=0;i<waveForms.length;i++) createSurfer(waveForms.item(i))

	// ========================================
	//Initates wavesurfer and attaches controls
	var createSurfer = function(waveform, url) {

		//Initate wave surfer
		wavesurfer = waveform.getElementsByClassName('wave');
		url = waveform.getAttribute('data-url');

		var wavesurfer = WaveSurfer.create({
			container: wavesurfer.item(0),
			scrollParent: false,
			waveColor: '#fff',
			progressColor: '#555',
			height: 300
		});
		wavesurfer.load(url);

		//Attach controls
		var playToggle = function() {
			// check play status
			if (wavesurfer.isPlaying()) {
				wavesurfer.pause()
			} else {
				wavesurfer.play()
			}
		}

		

	}


//})