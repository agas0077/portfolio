const projectNumIncrement = 2;

function getHiddenProjects() {
  return [].slice.call(document.querySelectorAll(".project-card[hidden]"));
}

function displayHidden() {
  projectToDisplay = getHiddenProjects().slice(0, projectNumIncrement);

  projectToDisplay.forEach((element) => {
    element.removeAttribute("hidden");
  });
}

const loadMoreButton = document.getElementById("load-more-projects-button");
loadMoreButton.addEventListener("click", (event) => {
  event.preventDefault();
  displayHidden();

  if (getHiddenProjects().length === 0) {
    loadMoreButton.setAttribute("disabled", "");
  }
});

displayHidden();
