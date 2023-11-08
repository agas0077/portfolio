const projectNumIncrement = 2;

function getHiddenProjects(buttonElement) {
  const cardsDiv = buttonElement.parentElement.parentElement;
  return [].slice.call(cardsDiv.querySelectorAll(".project-card[hidden]"));
}

function displayHidden(button) {
  projectToDisplay = getHiddenProjects(button).slice(0, projectNumIncrement);

  projectToDisplay.forEach((element) => {
    element.removeAttribute("hidden");
  });
}

const loadMoreButtons = [].slice.call(
  document.getElementsByClassName("load-more-projects-button")
);
loadMoreButtons.forEach((button) => {
  displayHidden(button);
  button.addEventListener("click", (event) => {
    event.preventDefault();
    displayHidden(button);

    if (getHiddenProjects(button).length === 0) {
      button.setAttribute("disabled", "");
    }
  });
});

