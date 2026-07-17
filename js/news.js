// =====================================================
// Azziano Marathi News - news.js
// =====================================================

const NEWS_FILE = "news.json";


// =====================================================
// Fix UTF-8 Marathi Mojibake
// =====================================================

function fixMarathiEncoding(text) {

    if (!text) return "";

    if (!text.includes("à")) {
        return text;
    }

    try {
        return decodeURIComponent(
            escape(text)
        );
    }
    catch(e) {
        return text;
    }
}

// =====================================================
// Format Date
// =====================================================

function formatDate(dateString) {

    if (!dateString) return "";

    let date = new Date(dateString);

    return date.toLocaleString("mr-IN", {

        day: "2-digit",
        month: "short",
        year: "numeric",
        hour: "2-digit",
        minute: "2-digit"

    });

}


// =====================================================
// Create News Card
// =====================================================

function createNewsCard(article) {


    let title = fixMarathiEncoding(article.title);


    return `

    <div class="news-card">

        <a href="${article.url}" target="_blank">

            <h3>${title}</h3>

        </a>


        <div class="news-meta">

            ${article.source?.name || ""}

            |

            ${formatDate(article.published)}

        </div>


    </div>

    `;

}


// =====================================================
// Display Category News
// =====================================================

function displayCategoryNews(id, articles) {


    let container = document.getElementById(id);


    if (!container) return;


    if (!articles || articles.length === 0) {

        container.innerHTML =
        "<p>बातम्या उपलब्ध नाहीत</p>";

        return;

    }


    container.innerHTML = articles

        .slice(0,5)

        .map(createNewsCard)

        .join("");

}



// =====================================================
// Featured News
// =====================================================

function displayFeatured(article) {


    let container =
        document.getElementById("featuredNews");


    if (!container || !article) return;


    let title =
        fixMarathiEncoding(article.title);


    container.innerHTML = `


    <div class="featured-card">


        <a href="${article.url}" target="_blank">


            <h2>

            ${title}

            </h2>


        </a>


        <p>

        ${article.source?.name || ""}

        |

        ${formatDate(article.published)}

        </p>


    </div>


    `;

}



// =====================================================
// Load News JSON
// =====================================================

async function loadNews() {


    try {


        const response =
            await fetch(NEWS_FILE);


        const data =
            await response.json();



        // Last Updated

        let update =
            document.getElementById("lastUpdated");


        if (update && data.lastUpdated) {

            update.innerHTML =
            "अपडेट : " + data.lastUpdated;

        }



        // Featured

        if (data.maharashtra?.length) {

            displayFeatured(
                data.maharashtra[0]
            );

        }



        // Categories

        displayCategoryNews(

            "maharashtraNews",

            data.maharashtra

        );


        displayCategoryNews(

            "indiaNews",

            data.india

        );


        displayCategoryNews(

            "worldNews",

            data.world

        );


        displayCategoryNews(

            "sportsNews",

            data.sports

        );


        displayCategoryNews(

            "businessNews",

            data.business

        );



    }

    catch(error) {


        console.error(
            "News loading error:",
            error
        );


        let box =
        document.getElementById("featuredNews");


        if (box) {

            box.innerHTML =
            "बातम्या लोड करताना त्रुटी आली.";

        }

    }

}



// =====================================================
// Start
// =====================================================

document.addEventListener(
    "DOMContentLoaded",
    loadNews
);