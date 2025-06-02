/** @format */

(function () {
  let k = window.Kapa;
  if (!k) {
    let i = function () {
      i.c(arguments);
    };
    i.q = [];
    i.c = function (args) {
      i.q.push(args);
    };
    window.Kapa = i;
  }
})();

// keeps MkDocs from seeing the keydown
function stopMkdocsShortcuts(e) {
  if (e.ctrlKey || e.metaKey || e.altKey) return;
  const blocked = new Set(['/', 's', 'f', 'n', 'p', '.']);
  if (blocked.has(e.key.toLowerCase())) {
    e.stopImmediatePropagation();
  }
}

Kapa('onModalOpen', () => {
  window.addEventListener('keydown', stopMkdocsShortcuts, true);
});

Kapa('onModalClose', () => {
  window.removeEventListener('keydown', stopMkdocsShortcuts, true);
});

document.addEventListener('DOMContentLoaded', function () {
  var script = document.createElement('script');
  script.src = 'https://widget.kapa.ai/kapa-widget.bundle.js';
  script.setAttribute(
    'data-website-id',
    'd4477ef9-8d35-448e-b5ea-3b8f13d1cf1e'
  );
  script.setAttribute('data-project-name', 'Polygon');
  script.setAttribute('data-project-color', '#6306B6');
  script.setAttribute(
    'data-project-logo',
    'https://polygontechnology.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F51562dc1-1dc5-4484-bf96-2aeac848ae2f%2F2c578a74-e8a1-4b2d-aafa-3126339715ae%2FPolygon_Icon_White_Purple_Rn.png?id=f3d302a7-607b-4f4d-8490-240c7eafe3c7&table=block&spaceId=51562dc1-1dc5-4484-bf96-2aeac848ae2f&width=2000&userId=&cache=v2'
  );
  script.setAttribute('data-button-image-height', '2rem');
  script.setAttribute('data-button-image-width', '2.5rem');
  script.setAttribute('data-modal-open-by-default', 'false');
  script.setAttribute('data-modal-title', 'Polygon Docs Chat Bot');
  script.setAttribute('data-modal-example-questions-title', 'Try asking me...');
  script.setAttribute('data-font-size-sm', '.7rem');
  script.setAttribute('data-query-input-font-size', '0.80rem');
  script.setAttribute('data-modal-disclaimer-font-size', '0.6rem');
  script.setAttribute('data-modal-title-font-size', '1.1rem');
  script.setAttribute("data-example-question-button-font-size","0.6rem");
  script.setAttribute("data-user-analytics-cookie-enabled","true");
  script.setAttribute(
    'data-modal-disclaimer',
    'This AI chatbot is powered by kapa.ai. Responses are generated automatically and may be inaccurate or incomplete. Do not rely on this information as legal, financial or other professional advice. By using this assistant, you agree that your input may be processed in accordance with the kapa.ai privacy policy: https://www.kapa.ai/content/privacy-policy'
  );
  script.setAttribute(
    'data-modal-example-questions',
    'What is the finality time on Polygon?, How do I connect my wallet to Polygon?'
  );
  script.setAttribute('data-button-text-color', '#ffffff');
  script.setAttribute('data-modal-title-color', '#ffffff');
  script.setAttribute('data-modal-header-bg-color', '#6306B6');
  script.setAttribute('data-button-position-top', '10px');
  script.setAttribute('data-button-position-right', '20px');
  script.setAttribute('data-button-text-font-size', '0.8rem');
  script.setAttribute('data-button-height', '3.8rem');
  script.setAttribute('data-button-width', '3.6rem');
  script.async = true;
  document.head.appendChild(script);
});
