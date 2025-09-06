<template>
  <div class="page-container" v-if="recipe">
    <div class="card">
      <!-- Top Image -->
      <img
        v-if="recipe.image"
        :src="recipe.image"
        alt="Recipe Image"
        class="recipe-img"
      />

      <!-- Content -->
      <div class="card-content">
        <button class="back-btn" @click="$router.back()">⬅ Back</button>

        <h1 class="recipe-title">{{ recipe.name }}</h1>
        <div class="meta">
          <span class="badge">🕒 {{ recipe.minutes }} mins</span>
          <span v-if="recipe.calories" class="badge fire">🔥 {{ Math.round(recipe.calories) }} cal</span>
        </div>

        <section class="ingredients">
          <h3>🛒 Ingredients</h3>
          <ul>
            <li v-for="ing in recipe.ingredients_list" :key="ing">{{ ing }}</li>
          </ul>
        </section>

        <section class="steps">
          <h3>👨‍🍳 Steps</h3>
          <ol>
            <li v-for="s in recipe.steps_list" :key="s">{{ s }}</li>
          </ol>
        </section>
         <RecipeFeedback :recipeId="recipe.id" />
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import RecipeFeedback from "@/components/RecipeFeedback.vue";

export default {
  props: ["id"],
  components: { RecipeFeedback },
  data() {
    return {
      recipe: null,
    };
  },
  async created() {
    try {
      const res = await axios.get(`/api/recipe/${this.$route.params.id}`);
      this.recipe = res.data.recipe;
    } catch (err) {
      console.error(err);
    }
  },
};
</script>

<style scoped>
.page-container {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: flex-start;
  padding: 2rem;
  min-height: 100vh;

  /* Background image */
    background: url("../assets/images/78900.jpg");
}

.page-container::before {
  content: "";
  position: absolute;
  inset: 0;
  background: rgba(0, 0, 0, 0.55);  
  backdrop-filter: blur(4px);         
  z-index: 0;
}

.card {
  max-width: 900px;
  width: 100%;
  background: #242323;
  border-radius: 18px;
  overflow: hidden;
  box-shadow: 0 6px 18px rgba(0, 0, 0, 0.08);
  display: flex;
  flex-direction: column;
  position: relative;
  z-index: 1;
}

.recipe-img {
  width: 100%;
  height: 280px;
  object-fit: cover;
}

.card-content {
  padding: 1.5rem;
}

.back-btn {
  background: transparent;
  border: none;
  color: #b8afaf;
  font-size: 0.95rem;
  cursor: pointer;
  margin-bottom: 1rem;
  transition: color 0.2s ease;
}
.back-btn:hover {
  color:  #e46930;
}

.recipe-title {
  font-size: 2rem;
  font-weight: 700;
  margin: 0.5rem 0 1rem 0;
  color: #e46930;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.meta {
  display: flex;
  gap: 0.6rem;
  margin-bottom: 1.5rem;
}

.badge {
  font-size: 0.9rem;
  padding: 0.35rem 0.75rem;
  border-radius: 12px;
  background: #f3f4f6;
  color: #1f1e1e;
  font-weight: 500;
  background: #2d2d2e;
  color: #ffffff;
   border: 1px solid rgba(252, 251, 251, 0.308);
}

.badge.fire {
  /* background: #ffe9e9;
  color: #e63946; */
  /* font-weight: 600; */
}

section {
  margin-top: 1.5rem;
}

section h3 {
  font-size: 1.2rem;
  font-weight: 600;
  margin-bottom: 0.6rem;
  color: #e46930;
}

ul, ol {
  margin: 0;
  padding-left: 1.2rem;
}

ol{
   margin-bottom: 100px;
}

li {
  margin-bottom: 0.4rem;
  line-height: 1.5;
  color: #f3f4f6;
  font-size: 1.1rem;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
</style>
