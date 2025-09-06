<template>
  <div class="feedback-container">
    <p class="feedback-title">Was this recipe helpful?</p>
    <div class="btn-group">
      <button
        class="feedback-btn useful"
        @click="sendFeedback(1)"
        :disabled="submitted"
      >
        👍 Useful
      </button>
      <button
        class="feedback-btn not-useful"
        @click="sendFeedback(0)"
        :disabled="submitted"
      >
        👎 Not Useful
      </button>
    </div>
    <p v-if="submitted" class="thanks-msg">Thanks for your feedback! 🙌</p>
  </div>
</template>

<script>
import axios from "axios";

export default {
  props: {
    recipeId: { type: Number, required: true },
    query: { type: String, default: "" }, // in case you want to log the search query
  },
  data() {
    return {
      submitted: false,
    };
  },
  methods: {
    async sendFeedback(helpful) {
      try {
        await axios.post("/api/feedback", {
          recipe_id: this.recipeId,
          query: this.query,
          helpful: helpful,
        });
        this.submitted = true;
      } catch (err) {
        console.error("Feedback error:", err);
      }
    },
  },
};
</script>

<style scoped>
.feedback-container {
  margin-top: 2rem;
  text-align: center;
}

.feedback-title {
  font-weight: 600;
  margin-bottom: 0.8rem;
  color: #dbdbdb;
}

.btn-group {
  display: flex;
  justify-content: center;
  gap: 1rem;
}

.feedback-btn {
  padding: 0.6rem 1.2rem;
  font-size: 1rem;
  border-radius: 10px;
  border: none;
  cursor: pointer;
  transition: all 0.2s ease;
    background: #2d2d2e;
  color: #ffffff;
   border: 1px solid rgba(252, 251, 251, 0.308);
}

.feedback-btn.useful {
  /* background: #d1fae5; */
  color: #fcfcfc;
}
.feedback-btn.useful:hover {
  background: #e46930;
}

.feedback-btn.not-useful {
  /* background: #fee2e2; */
  color: #f8f8f8;
}
.feedback-btn.not-useful:hover {
  background: #e46930;
}

.feedback-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.thanks-msg {
  margin-top: 1rem;
  color: #16a34a;
  font-weight: 500;
}
</style>
