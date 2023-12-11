<style>
    .feature-paragraph {
        text-align: left;
    }
   .md-sidebar.md-sidebar--secondary,
   .md-content__button {
   display: none;
   }
   * {
   box-sizing: border-box;
   }
   .grid-container {
   display: flex;
   flex-wrap: wrap;
   width: 100%;
   padding: 10px;
   align-items: stretch;
   }
   .grid-item {
   background-color: hsla(0,0%,100%,0);
   border-radius: 8px;
   -webkit-box-shadow: 0 8px 16px 0 rgb(17 17 17 / 8%);
   box-shadow: 0 8px 16px 0 rgb(17 17 17 / 8%);
   padding: 33px;
   margin: 5px;
   text-align: center;
   align-items: center;
   flex: 32%;
   width: 32%;  
   }
   @media screen and (max-width: 1000px) {
   .grid-item {
   flex: 32%;
   max-width: 32%;
   }
   }
   @media screen and (max-width: 800px) {
   .grid-item {
   flex: 48%;
   max-width: 48%;
   }
   }
   @media screen and (max-width: 600px) {
   .grid-item {
   flex: 100%;
   max-width: 100%;
   }
   }
</style>
   <div class="section-wrapper product-section-head">
         <div class="hero-image"><img src="../img/home/main-img.svg" loading="lazy" class="hero-image" style="width: 40%; float: right;"></div>
      <div class="hero-left">
         <h1 class="hero-heading">Tools</h1>
         <p class="hero-subtext">This section of the documentation describes some of the available third-party tools used by developers with Polygon products and services.</p>
         <p class="hero-subtext">Find out how to access data, code against blockchain networks, use data oracles, and much more. </p>
      </div>
   </div>
   <div class="grid-container">
      <div class="grid-item">
         <a href="./smart-contracts/hardhat">
            <div class="product-list-item-header">
               <div class="feature-card-heading">Smart contracts</div>
            </div>
            <p class="feature-paragraph">Common software for designing, building, and deploying smart contracts.</p>
         </a>
      </div>
      <div class="grid-item">
         <a href="./gas/matic-faucet">
            <div class="product-list-item-header">
               <div class="feature-card-heading">Gas</div>
            </div>
            <p class="feature-paragraph">The Polygon MATIC gas faucet and gas estimation tools.</p>
         </a>
      </div>
      <div class="grid-item">
         <a href="./data/the-graph/overview">
            <div class="product-list-item-header">
               <div class="feature-card-heading">Data</div>
            </div>
            <p class="feature-paragraph">Software tools, such as Graph, used for efficient data manipulation on Polygon networks.</p>
         </a>
      </div>
      <div class="grid-item">
         <a href="./matic-js/get-started">
            <div class="product-list-item-header">
               <div class="feature-card-heading">MaticJS</div>
            </div>
            <p class="feature-paragraph">The <code>matic.js</code> library used to interact with Polygon networks and services.</p>
         </a>
      </div>
      <div class="grid-item">
         <a href="./storage/ipfs">
            <div class="product-list-item-header">
               <div class="feature-card-heading">Storage</div>
            </div>
            <p class="feature-paragraph">Interact with blockchain storage services such as IPFS.</p>
         </a>
      </div>
      <div class="grid-item">
         <a href="./oracles/getting-started">
            <div class="product-list-item-header">
               <div class="feature-card-heading">Oracles</div>
            </div>
            <p class="feature-paragraph">Oracle services used for accessing accurate offline data.</p>
         </a>
      </div>
      <div class="grid-item">
         <a href="./wallets/getting-started">
            <div class="product-list-item-header">
               <div class="feature-card-heading">Wallets</div>
            </div>
            <p class="feature-paragraph">Using Polygon-compatible external wallets, such as MetaMask, with Polygon networks.</p>
         </a>
      </div>
      <div class="grid-item">
         <a href="https://polygonscan.com/">
            <div class="product-list-item-header">
               <div class="feature-card-heading">Block explorers</div>
            </div>
            <p class="feature-paragraph">Quick links to useful block explorers such as https://polygonscan.com/ for example.</p>
         </a>
      </div>
   </div>
   </div>
   <script src="https://d3e54v103j8qbb.cloudfront.net/js/jquery-3.5.1.min.dc5e7f18c8.js?site=6569b132e06e045d402ee3ac" type="text/javascript" integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0=" crossorigin="anonymous"></script>