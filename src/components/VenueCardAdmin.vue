<template>
    <DeleteConfirm v-if="deleteConfirmationVisible" @onDelete="deleteVenue" @hideDelete="deleteConfirmation" />
    <EditVenueModal :showVenueModal="showEditVenue" @editVenue="editVenue" @closeModal="hideEditVenueModal" :title="'Edit'"
        :editVenue="venue" />
    <AddShowModal :showShowModal="showAddShow" @addShow="addShow" @closeModal="hideAddShowModal" :title="'Add New'" />
    <div class="containerV">
        <div class="venue-card-admin">
            <h2>{{ venue.name }}</h2>
            <h6>{{ venue.place }}, {{ venue.location }}</h6>

            <button @click="showAddShowModal" class="addButtonV">+</button>
            <br />
            <div class="shows-container-admin">
                <ShowCard v-for="show in shows" :key="show.id" :show="show" />
            </div>
            <br />

            <div class="venue-card-admin-footer">
                <button @click="showEditVenueModal">Edit</button>
                <button @click="() => deleteConfirmation(true)">Delete</button>
            </div>
        </div>
    </div>
</template>

<script>
import DeleteConfirm from './DeleteConfirm.vue';
import ShowCard from './ShowCardAdmin.vue';
import AddShowModal from './ShowModal.vue';
import EditVenueModal from './VenueModal.vue';


export default {
    data: () => {
        return {
            shows: [],
            showEditVenue: false,
            showAddShow: false,
            deleteConfirmationVisible: false,
        }
    },
    props: ['venue'],
    components: {
        ShowCard,
        // eslint-disable-next-line vue/no-unused-components
        AddShowModal,
        EditVenueModal,
        DeleteConfirm
    },
    methods: {
        showEditVenueModal() {
            this.showEditVenue = true;
        },
        hideEditVenueModal() {
            this.showEditVenue = false;
        },
        showAddShowModal() {
            this.showAddShow = true;
        },
        hideAddShowModal() {
            this.showAddShow = false;
        },
        deleteConfirmation(e) {
            this.deleteConfirmationVisible = e;
        },
        async addShow(newShow) {
            newShow.venue = this.venue.name;
            const rawResponse = await fetch(`http://127.0.0.1:8081/api/show`, {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                    'access-token': localStorage.getItem("token")
                },
                body: JSON.stringify(newShow),
            });
            console.log(rawResponse)
            this.$emit('onUpdate');
        },
        async editVenue(editVenue) {
            console.log(JSON.stringify(editVenue))
            console.log(this.venue)
            const rawResponse = await fetch(`http://127.0.0.1:8081/api/venue/${this.venue.venue_id}`, {
                method: 'PUT',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                    'access-token': localStorage.getItem("token")
                },
                body: JSON.stringify(editVenue)
            });
            console.log(rawResponse)
            this.$emit('onUpdate');
        },
        async deleteVenue() {
            const rawResponse = fetch(`http://127.0.0.1:8081/api/venue/${this.venue.venue_id}`, {
                method: 'DELETE',
                headers: {
                    'access-token': localStorage.getItem("token")
                }
            })
            console.log('Delete venue:', rawResponse);
            this.deleteConfirmation(false);
        },
    },
    async mounted() {
        try {
            const getVenueShow = await fetch(`http://127.0.0.1:8081/api/getVenueShow/${this.venue.venue_id}`,
                {
                    headers: {
                        'access-token': localStorage.getItem("token")
                    }
                }
            );
            const showsData = await getVenueShow.json();
            this.shows = Object.values(showsData).pop();
        } catch (error) {
            console.error('Error fetching venues:', error);
        }
    }
};
</script>

<style>
.venue-card-admin {
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    background-color: white;
    width: max-content;
    padding: 20px;
    border-radius: 10px;
}

.containerV {
    max-height: 100%;
    margin: 10px;
    border-radius: 10px;
    padding: 20px;
    background-color: cornflowerblue;
}

.venue-card-admin button {
    background: white;
    border: 1px solid black;
    padding: 5px;
    margin: 5px;
}

.addButtonV {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 40px;
    height: 40px;
    border-radius: 120px;
    background-color: aqua;
    font-size: x-large;
}

.shows-container-admin {
    max-height: 100%;
    overflow: auto;
}

.venue-card-admin-footer>button {
    border-radius: 10px;
}
</style>
