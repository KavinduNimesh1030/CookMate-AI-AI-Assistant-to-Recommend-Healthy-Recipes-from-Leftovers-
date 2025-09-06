<template>
  <div class="top-feedback">
    <h2>🔥 Top Rated by Users</h2>
    <div class="results">
      <RecipeCard
        v-for="recipe in recipes"
        :key="recipe.id"
        :recipe="recipe"
        @click="$emit('select', recipe.id)"
      />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import RecipeCard from "./RecipeCard.vue";

export default {
  components: { RecipeCard },
  data() {
    return {
      recipes: [],
    };
  },
  async created() {
    try {
      const res = await axios.get("/api/top-feedback");
      this.recipes = res.data.recipes;
    } catch (err) {
      console.error("Failed to load top feedback recipes", err);
    }
  },
};
</script>

<style>
.top-feedback {
  margin: 2rem 0;
}
.top-feedback h2 {
  color: #ff6a00;
  margin-bottom: 1rem;
  text-align: center;
}
.results {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 1.5rem;
}
</style>
