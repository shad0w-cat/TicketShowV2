<template>
  <div>
    <div class="delete-confirmation">
      <div class="delete-confirmation-box">
        <h3>Confirm Delete</h3>
        <p>Are you sure you want to delete this item?</p>
        <div class="delete-buttons">
          <button @click="handleDelete">Delete</button>
          <button @click="hideDeleteConfirmation">Cancel</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
    };
  },
  methods: {
    handleDelete() {
      this.$emit('onDelete');
    },
    hideDeleteConfirmation() {
      this.$emit('hideDelete', false);
    },
  },
};
</script>

<style>
/* Add your custom styles for the delete confirmation here */
.delete-confirmation {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.7);
  display: flex;
  justify-content: center;
  align-items: center;
}

.delete-confirmation-box {
  background-color: #fff;
  padding: 20px;
  border-radius: 4px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  max-width: 400px;
}

.delete-confirmation-box h3 {
  margin: 0 0 10px;
}

.delete-buttons {
  display: flex;
  justify-content: flex-end;
}

.delete-buttons button {
  margin-left: 10px;
}
</style>