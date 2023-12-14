---
hide:
- toc
---

<style>
    .feature-paragraph {
        text-align: left;
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
   background-color: white;
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
         <div class="hero-image"><img src="../img/miden/miden.svg" loading="lazy" class="hero-image" style="width: 40%; float: right;"></div>
      <div class="hero-left">
         <h1 class="hero-heading">Polygon Miden</h1>
         <h2><code>Software in development</code></h2>
         <h2></h2>
         <p class="hero-subtext">Polygon Miden is an in-development zero-knowledge (zk) rollup running on the Miden VM, a virtual machine that prioritizes zk-friendliness over EVM compatibility.</p>
      </div>
   </div>
   <div class="grid-container">
      <div class="grid-item">
         <a href="./introduction/">
            <div class="product-list-item-header">
               <div class="feature-card-heading">zkRollup docs</div>
            </div>
            <p class="feature-paragraph">The Miden zkRollup docs detail the current state of the development and design.</p>
         </a>
      </div>
      <div class="grid-item">
         <a href="./roadmap">
            <div class="product-list-item-header">
               <div class="feature-card-heading">zkRollup roadmap</div>
            </div>
            <p class="feature-paragraph">Check out the Miden zkRollup roadmap for the latest updates.</p>
         </a>
      </div>
      <div class="grid-item">
         <a href="https://0xpolygonmiden.github.io/miden-vm/intro/main.html">
            <div class="product-list-item-header">
               <div class="feature-card-heading">Miden VM</div>
            </div>
            <p class="feature-paragraph">Check out the Miden zero-knowledge virtual machine documentation.</p>
         </a>
      </div>
   </div>
   </div>