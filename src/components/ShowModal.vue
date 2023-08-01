<template>
    <div v-if="showShowModal" class="add-show-modal">
        <div class="show-modal-content">
            <h3>{{ title }} Show</h3>
            <form @submit.prevent="addShow">
                <div class="form-group">
                    <label for="show_name">Show Name:</label>
                    <input type="text" id="show_name" v-model="newShow.showName" required>
                    <label for="price">Price:</label>
                    <input type="number" id="price" v-model="newShow.place" min="1" required>
                    <label for="availableSeats">Available Seats:</label>
                    <input type="number" id="availableSeats" v-model="newShow.available_seats" required>
                    <label for="rating">Rating:</label>
                    <input type="text" id="rating" v-model="newShow.capacity" required>
                    <label for="tags">Tags:</label>
                    <input type="text" id="tags" v-model="newShow.tags" required>
                </div>
                <div class="form-btns">
                    <button type="submit">{{ title }} Show</button>
                    &nbsp;
                    <button @click.prevent="hideModal">Cancel</button>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        if (this.editShow) {
            return {
                newShow: {
                    showName: this.editShow.name,
                    price: this.editShow.place,
                    available_seats: this.editShow.available_seats,
                    rating: this.editShow.rating,
                    tags: this.editShow.tags,
                },
            };
        }
        else {
            return {
                newShow: {
                    showName: '',
                    price: '',
                    available_seats: '',
                    rating: 0,
                    tags: '',
                },
            };
        }
    },
    methods: {
        addShow() {
            if (this.title === "Edit") {
                console.log(this.newShow)
                this.$emit('editShow', this.newShow);
            }
            else
                this.$emit('addShow', this.newShow);
            this.hideModal();
            this.resetForm();
        },
        hideModal() {
            this.resetForm();
            this.$emit('closeModal');
        },
        resetForm() {
            if (this.editShow) {
                this.newShow = {
                    showName: this.editShow.name,
                    price: this.editShow.place,
                    available_seats: this.editShow.available_seats,
                    rating: this.editShow.rating,
                    tags: this.editShow.tags,
                };
            }
            else {
                this.newShow = {
                    showName: '',
                    price: '',
                    available_seats: '',
                    rating: 0,
                    tags: '',
                };
            }
        },
    },
    props: {
        title: {
            type: String,
            required: true,
        },
        showShowModal: {
            type: Boolean,
            required: true,
        },
        editShow: {
            type: Object,
            required: false,
        }
    },
};
</script>

<style>
.add-show-modal {
    z-index: 1;
    background-color: #0f0f0f6c;
    position: absolute;
    top: 0%;
    left: 0%;
    height: 100%;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}

.show-modal-content {
    background-color: aliceblue;
    padding: 2%;
    border-radius: 10px;
}

.form-group>* {
    padding: 7px;
    margin-block: 10px;
}

.form-group {
    display: grid;
    grid-template-columns: 50% 50%;
}

.form-btns {
    margin-top: 10px;
    display: flex;
    justify-content: flex-end;
}

.form-btns>* {
    padding: 5px;
}
</style>
