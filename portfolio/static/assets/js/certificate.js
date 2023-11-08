// Adds certificate pop ups
const educationButtonList = [].slice.call(document.getElementsByClassName('education-btn'));
educationButtonList.map(function (element) {
    element.addEventListener('click', (event) => {
        const modal = document.getElementById("modal-body-id");

        var id = event.target.id;
        var placeholder = document.createElement("div");
        placeholder.classList.add("spinner-border");
        placeholder.classList.add("text-primary");
        placeholder.setAttribute("role", "status");
        modal.appendChild(placeholder);

        var xhr = new XMLHttpRequest();
        let url = window.location.origin + "/candidate/certificate?pk=" + id

        xhr.open("GET", url, true);
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                var response = JSON.parse(xhr.responseText);
                var pdfBlock = document.createElement("embed");
                pdfBlock.setAttribute("type", "application/pdf");
                pdfBlock.setAttribute("width", "100%");
                pdfBlock.setAttribute("height", "100%");
                pdfBlock.setAttribute("src", response.url);
                if (modal.hasChildNodes()) {
                    const modalChildren = [].slice.call(modal.childNodes);
                    modalChildren.map((child) => { modal.removeChild(child) })
                }
                modal.appendChild(pdfBlock);
            }
        };
        xhr.send();

    });
});
