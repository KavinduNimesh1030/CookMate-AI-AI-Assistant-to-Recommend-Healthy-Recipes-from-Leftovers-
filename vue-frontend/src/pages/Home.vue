<template>
  <div class="container">
    <div class="hero">
      <h1>🍲 Healthy Recipe Finder</h1>
      <p>Discover delicious recipes using what you have at home!</p>
    </div>

    <form @submit.prevent="searchRecipes" class="search-form">
      <input v-model="query" type="text" placeholder="Enter ingredients..." />
      <label class="checkbox-lable">
        <input type="checkbox" v-model="healthy" /> Prefer healthier
      </label>
      <button type="submit">Search</button>
    </form>

    <div v-if="loading" class="loading">Searching...</div>

    <div class="results">
      <RecipeCard
        v-for="recipe in results"
        :key="recipe.id"
        :recipe="recipe"
        @click="goToRecipe(recipe.id)"
      />
    </div>
    <TopFeedbackRecipes @select="goToRecipe" />
  </div>
</template>

<script>
import axios from "axios";
import RecipeCard from "../components/RecipeCard.vue";
import TopFeedbackRecipes from "../components/TopFeedbackRecipes.vue";

export default {
  components: { RecipeCard, TopFeedbackRecipes },
  data() {
    return {
      query: "",
      healthy: false,
      results: [],
      loading: false,
    };
  },
  created() {
    const { q, healthy } = this.$route.query;
    if (q) {
      this.query = q;
      this.healthy = healthy === "1";
      this.searchRecipes();
    }
  },

  methods: {
    // async searchRecipes() {
    //   this.loading = true;
    //   this.results = [];
    //   try {
    //     const res = await axios.post("/api/search", {
    //       query: this.query,
    //       healthy: this.healthy,
    //     });
    //     this.results = res.data.results;
    //   } catch (err) {
    //     console.error(err);
    //   } finally {
    //     this.loading = false;
    //   }
    // },
    async searchRecipes() {
      this.loading = true;
      this.results = [];
      try {
        // push query + healthy into URL
        this.$router.push({
          path: "/",
          query: { q: this.query, healthy: this.healthy ? 1 : 0 },
        });

        const res = await axios.post("/api/search", {
          query: this.query,
          healthy: this.healthy,
        });
        this.results = res.data.results;
      } catch (err) {
        console.error(err);
      } finally {
        this.loading = false;
      }
    },
    goToRecipe(id) {
      this.$router.push(`/recipe/${id}`);
    },
  },
};
</script>

<style>
/* General container */
.container {
  /* max-width: 100%; */
  margin: auto;
  padding: 2rem;
  font-family: "Poppins", sans-serif;
  color: #333;
  background: linear-gradient(135deg, #000000, #635f5e);
  /* border-radius: 15px; */
  box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
}

/* Hero section */
.hero {
  text-align: center;
  margin-bottom: 2rem;
  padding: 2rem;
  background: url("https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=900&q=80")
    center/cover no-repeat;
  border-radius: 15px;
  color: #fff;
  text-shadow: 1px 1px 10px rgba(0, 0, 0, 0.6);
}
.hero h1 {
  font-size: 3rem;
  margin-bottom: 0.5rem;
}
.hero p {
  font-size: 1.2rem;
}

/* Search form */
.search-form {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  justify-content: center;
  margin-bottom: 2rem;
}
.search-form input[type="text"] {
  flex: 1;
  padding: 0.8rem 1rem;
  border-radius: 10px;
  border: none;
  /* box-shadow: 0 5px 15px rgba(0,0,0,0.1); */
  transition: all 0.3s ease;
  background-color: #333;
  border: 1px solid rgb(247, 118, 12);
  color: #fff;
}
.search-form input[type="text"]:focus {
  outline: none;
  box-shadow: 0 5px 20px rgba(247, 118, 12, 0.2);
  backdrop-filter: blur(4px);
}
.search-form label {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.95rem;
}
.search-form button {
  padding: 0.8rem 2rem;
  border: none;
  border-radius: 10px;
  background: linear-gradient(45deg, #ff6a00, #ff8e53);
  color: #fff;
  font-weight: bold;
  cursor: pointer;
  transition: all 0.3s ease;
}
.search-form button:hover {
  transform: translateY(-3px);
  box-shadow: 0 10px 20px rgba(255, 105, 180, 0.4);
}

/* Loading */
.loading {
  text-align: center;
  font-weight: bold;
  font-size: 1.2rem;
  margin-bottom: 1rem;
  color: #ff6a00;
  animation: pulse 1s infinite;
}
.checkbox-lable {
  color: #ff6a00;
}
@keyframes pulse {
  0%,
  100% {
    opacity: 1;
  }
  50% {
    opacity: 0.6;
  }
}

/* Results grid */
.results {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 1.5rem;
}

/* Recipe card */
.results ::v-deep(.recipe-card) {
  border-radius: 15px;
  overflow: hidden;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s, box-shadow 0.3s;
}
.results ::v-deep(.recipe-card:hover) {
  transform: translateY(-5px);
  box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
}
.results ::v-deep(.recipe-card img) {
  width: 100%;
  height: 180px;
  object-fit: cover;
  filter: brightness(0.9);
  transition: filter 0.3s;
}
.results ::v-deep(.recipe-card:hover img) {
  filter: brightness(1);
}
.results ::v-deep(.recipe-card .info) {
  padding: 1rem;
  background: #fff;
}
.results ::v-deep(.recipe-card .info h2) {
  font-size: 1.2rem;
  margin-bottom: 0.5rem;
}
.results ::v-deep(.recipe-card .info p) {
  font-size: 0.95rem;
  color: #666;
}
</style>
