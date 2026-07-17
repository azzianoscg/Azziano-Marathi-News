/* ==========================================================
   AZZIANO MARATHI NEWS
   accordion.js
   Version 2.0
========================================================== */

"use strict";

/* ----------------------------------------------------------
   Initialize Accordion
---------------------------------------------------------- */

function initializeAccordion() {

    const headers = document.querySelectorAll(".accordion-header");

    headers.forEach(header => {

        header.addEventListener("click", () => {

            toggleAccordion(header);

        });

    });

}

/* ----------------------------------------------------------
   Toggle Accordion
---------------------------------------------------------- */

function toggleAccordion(selectedHeader) {

    const allHeaders = document.querySelectorAll(".accordion-header");
    const allBodies = document.querySelectorAll(".accordion-body");

    const selectedBody = selectedHeader.nextElementSibling;
    const isOpen = selectedBody.classList.contains("open");

    // Close all sections
    allHeaders.forEach(header => {

        header.classList.remove("active");

        const arrow = header.querySelector(".arrow");
        if (arrow) {
            arrow.textContent = "▶";
        }

    });

    allBodies.forEach(body => {

        body.classList.remove("open");

        body.style.maxHeight = null;

    });

    // If already open, keep everything closed
    if (isOpen) {
        return;
    }

    // Open selected section
    selectedHeader.classList.add("active");

    const arrow = selectedHeader.querySelector(".arrow");

    if (arrow) {
        arrow.textContent = "▼";
    }

    selectedBody.classList.add("open");

    selectedBody.style.maxHeight =
        selectedBody.scrollHeight + "px";

    // Smoothly scroll into view
    setTimeout(() => {

        selectedHeader.scrollIntoView({

            behavior: "smooth",
            block: "start"

        });

    }, 150);

}

/* ----------------------------------------------------------
   Expand First Section
---------------------------------------------------------- */

function openFirstAccordion() {

    const firstHeader =
        document.querySelector(".accordion-header");

    if (firstHeader) {

        toggleAccordion(firstHeader);

    }

}

/* ----------------------------------------------------------
   Refresh Height
   (Call after loading news dynamically)
---------------------------------------------------------- */

function refreshAccordion() {

    const openBody =
        document.querySelector(".accordion-body.open");

    if (!openBody) return;

    openBody.style.maxHeight =
        openBody.scrollHeight + "px";

}