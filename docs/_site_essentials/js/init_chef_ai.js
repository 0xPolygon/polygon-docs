(function () {
    function initChefAi() {
      const PUBLIC_API_KEY =
        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NWQxNWI0YTUyNTcyZmMzMDI2ODg1OTgiLCJpYXQiOjE3MDgyMTkyMTAsImV4cCI6MjAyMzc5NTIxMH0.kjO3jaiDucVtCmF-665MVeRBd-VBm5MYYvwrzoIfVyQ";
  
      let cookbookContainer = document.getElementById("__cookbook");
      if (!cookbookContainer) {
        cookbookContainer = document.createElement("div");
        cookbookContainer.id = "__cookbook";
        cookbookContainer.dataset.apiKey = PUBLIC_API_KEY;
        document.body.appendChild(cookbookContainer);
      }
  
      let cookbookScript = document.getElementById("__cookbook-script");
      if (!cookbookScript) {
        cookbookScript = document.createElement("script");
        cookbookScript.id = "__cookbook-script";
        cookbookScript.src =
          "https://cdn.jsdelivr.net/npm/@cookbookdev/docsbot/dist/standalone/index.cjs.js";
        cookbookScript.async = true;
        document.head.appendChild(cookbookScript);
      }
  
      const keyPressPropagationBlocker = function (e) {
        e.stopPropagation();
      };
  
      document.addEventListener("cookbook:modal:state:change", function (e) {
        const isOpen = e.detail.isOpen;
        if (isOpen) {
          document.body.addEventListener("keydown", keyPressPropagationBlocker, {
            capture: true,
          });
        } else {
          document.body.removeEventListener(
            "keydown",
            keyPressPropagationBlocker,
            { capture: true }
          );
        }
      });
    }
  
    if (document.readyState === "complete") {
      initChefAi();
    } else {
      window.addEventListener("load", initChefAi);
    }
  })();