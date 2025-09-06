<template>
  <div class="card">
    <div class="card-header">
      <h3 class="title">{{ recipe.name }}</h3>
    </div>

    <div class="card-body">
      <div class="info">
        <span class="badge">🕒 {{ recipe.minutes }} mins</span>
        <span class="badge">🥗 {{ recipe.n_ingredients }} ingredients</span>
        <span v-if="recipe.calories" class="badge fire"
          >🔥 {{ Math.round(recipe.calories) }} cal</span
        >
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ["recipe"],
};
</script>

<style scoped>
.card {
  background: #3a3838;
  border-radius: 16px;
  padding: 1.2rem;
  box-shadow: 0 6px 14px rgba(0, 0, 0, 0.06);
  transition: transform 0.25s ease, box-shadow 0.25s ease;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  gap: 0.8rem;
  border: 1px solid rgb(247, 118, 12);
}

.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.12);
  background: linear-gradient(135deg, #e75f10, #e46930);
}

.card-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.title {
  font-size: 1.1rem;
  font-weight: 600;
  color: #ffffff;
  margin: 0;
  text-transform: capitalize;
}

.card-body {
  display: flex;
  flex-wrap: wrap;
  gap: 0.6rem;
}

.badge {
  font-size: 0.85rem;
  padding: 0.35rem 0.7rem;
  border-radius: 12px;
  background: #2d2d2e;
  color: #ffffff;
  font-weight: 500;
  display: inline-flex;
  align-items: center;
  gap: 1.25rem;
  margin: 2px;
  margin-bottom: 4px;
  border: 1px solid rgba(252, 251, 251, 0.308);
}

.badge.fire {
  background: #2d2d2e;
  color: #ffffff;
  font-weight: 600;
}
</style>
