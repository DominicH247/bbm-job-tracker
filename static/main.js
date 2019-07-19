

// Change colour of status indicator based on job status
function statusIndicator() {
	let getElement = document.getElementsByClassName('status-indicator')[0];
	let getChildText = getElement.innerText;
	let classChange; 
	if (getChildText == "Closed") {
		// getElement.className = "status-closed-indicator";
		classChange = getElement.className = "status-closed-indicator";
	} else if (getChildText == "Open") {
		classChange = getElement.className = "status-open-indicator";
	}
}



function tabStatus(){
	let classElements = document.getElementsByClassName('tab-status');
	for (var i = 0; i < classElements.length; i++){
		if (classElements[i].innerText == "Open"){
			classElements[i].className = "tab-status-open";
		} else if (classElements[i].innerText == "Closed"){
			classElements[i].className = "tab-status-closed";
		}
	}
}


function deadlineIndicator(){
	let classElements = document.getElementsByClassName('deadline-status');
	for (var i = 0; i < classElements.length; i++){
		if (classElements[i].innerText.indexOf("overdue!") != -1){
			classElements[i].className = "deadline-status-over";
		} else if (classElements[i].innerText.indexOf("until") != -1){
			classElements[i].className = "deadline-status-okay";
		}
	}
}

