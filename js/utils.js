/* ==========================================================
   AZZIANO MARATHI NEWS
   utils.js
   Version 2.0
========================================================== */

"use strict";

/* ----------------------------------------------------------
   Marathi Months
---------------------------------------------------------- */

const MARATHI_MONTHS = [
    "जानेवारी",
    "फेब्रुवारी",
    "मार्च",
    "एप्रिल",
    "मे",
    "जून",
    "जुलै",
    "ऑगस्ट",
    "सप्टेंबर",
    "ऑक्टोबर",
    "नोव्हेंबर",
    "डिसेंबर"
];

/* ----------------------------------------------------------
   Marathi Days
---------------------------------------------------------- */

const MARATHI_DAYS = [
    "रविवार",
    "सोमवार",
    "मंगळवार",
    "बुधवार",
    "गुरुवार",
    "शुक्रवार",
    "शनिवार"
];

/* ----------------------------------------------------------
   Convert English digits to Marathi digits
---------------------------------------------------------- */

function toMarathiNumber(value) {

    const digits = ['०','१','२','३','४','५','६','७','८','९'];

    return value
        .toString()
        .replace(/\d/g, d => digits[d]);

}

/* ----------------------------------------------------------
   Format Today's Date
---------------------------------------------------------- */

function formatTodayDate() {

    const today = new Date();

    const day =
        MARATHI_DAYS[today.getDay()];

    const date =
        toMarathiNumber(today.getDate());

    const month =
        MARATHI_MONTHS[today.getMonth()];

    const year =
        toMarathiNumber(today.getFullYear());

    return `📅 ${day}, ${date} ${month} ${year}`;

}

/* ----------------------------------------------------------
   Display Today's Date
---------------------------------------------------------- */

function showTodayDate() {

    const element =
        document.getElementById("todayDate");

    if (element) {

        element.textContent =
            formatTodayDate();

    }

}

/* ----------------------------------------------------------
   Update "Last Updated"
---------------------------------------------------------- */

function setLastUpdated(text) {

    const element =
        document.getElementById("lastUpdated");

    if (element) {

        element.textContent =
            "🕒 शेवटचे अद्यतन : " + text;

    }

}

/* ----------------------------------------------------------
   Open News Link
---------------------------------------------------------- */

function openNews(url) {

    if (!url) return;

    window.open(
        url,
        "_blank",
        "noopener,noreferrer"
    );

}

/* ----------------------------------------------------------
   Create HTML Element
---------------------------------------------------------- */

function createElement(tag, className = "") {

    const el =
        document.createElement(tag);

    if (className !== "") {

        el.className = className;

    }

    return el;

}

/* ----------------------------------------------------------
   Escape HTML
---------------------------------------------------------- */

function escapeHTML(text) {

    const div =
        document.createElement("div");

    div.textContent = text;

    return div.innerHTML;

}

/* ----------------------------------------------------------
   Show Loading
---------------------------------------------------------- */

function showLoading(containerId) {

    const container =
        document.getElementById(containerId);

    if (!container) return;

    container.innerHTML =

        `<div class="loading">
            बातम्या लोड होत आहेत...
        </div>`;

}

/* ----------------------------------------------------------
   Show Error
---------------------------------------------------------- */

function showError(containerId, message) {

    const container =
        document.getElementById(containerId);

    if (!container) return;

    container.innerHTML =

        `<div class="error">
            ${escapeHTML(message)}
        </div>`;

}

function startClock() {

    function updateClock() {

        const now = new Date();

        const time = now.toLocaleTimeString(
            "en-IN",
            {
                hour: "2-digit",
                minute: "2-digit",
                second: "2-digit",
                hour12: true
            }
        );

        document.getElementById("currentTime").textContent =
            "🕒 वर्तमान वेळ : " + time;

    }

    updateClock();

    setInterval(updateClock,1000);

}