<template>
    <DeleteConfirm v-if="deleteConfirmationVisible" @onDelete="deleteShow" @hideDelete="deleteConfirmation" />
    <EditShowModal :showShowModal="showEditShow" @editShow="editShow" @closeModal="hideEditShowModal" :title="'Edit'"
        :editShow="show" />
    <div class="containerS">
        <div class="show-card-admin">
            <h2>{{ show.name }}</h2>
            <div class="venue-card-admin-footer">
                <button @click="showEditShowModal">Edit</button>
                <button @click="() => deleteConfirmation(true)">Delete</button>
            </div>
        </div>
    </div>
</template>

<script>
import EditShowModal from './ShowModal.vue';
import DeleteConfirm from './DeleteConfirm.vue';


export default {
    data: () => {
        return {
            showEditShow: false,
            deleteConfirmationVisible: false,
        }
    },
    props: ['show'],
    components: {
        DeleteConfirm,
        // eslint-disable-next-line vue/no-unused-components
        EditShowModal,
    },
    methods: {
        deleteConfirmation(e) {
            this.deleteConfirmationVisible = e;
        },
        showEditShowModal() {
            this.showEditShow = true;
        },
        hideEditShowModal() {
            this.showEditShow = false;
        },
        async editShow(editShow) {
            console.log(JSON.stringify(editShow))
            const rawResponse = await fetch(`http://127.0.0.1:8081/api/show/${this.show.id}`, {
                method: 'PUT',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                    'access-token': localStorage.getItem("token")
                },
                body: JSON.stringify(editShow)
            });
            console.log(rawResponse)
            this.$emit('onUpdate');
        },
        async deleteShow() {
            const rawResponse = fetch(`http://127.0.0.1:8081/api/show/${this.show.id}`, {
                method: 'DELETE',
                headers: {
                    'access-token': localStorage.getItem("token")
                },
            })
            console.log('Delete venue:', rawResponse);
            this.deleteConfirmation(false);

        },
    },
};
</script>

<style>
.show-card-admin {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    background-color: white;
    width: max-content;
    padding: 20px;
    border-radius: 10px;
    width: 100%;
}

.containerS {
    margin: 10px;
    border-radius: 10px;
    padding: 20px;
    background-color: cornflowerblue;
}

.show-card-admin button {
    background: white;
    border: 1px solid black;
    padding: 5px;
    margin: 5px;
}

.addButtonS {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 40px;
    height: 40px;
    border-radius: 120px;
    background-color: aqua;
    font-size: x-large;
}

.show-card-admin-footer>button {
    border-radius: 10px;
}
</style>
