<template>
    <AlertComponent v-if="alert.show" :message="alert.message" :success="alert.success" @hide="hideAlert" />
    <div class="containerS">
        <div class="show-card-admin">
            <h2>{{ show.name }}</h2>
            <div class="venue-card-admin-footer">
                <button v-if="seats > 0" @click="bookShow">Book Show</button>
                <div v-else>Houseful 🎊</div>
            </div>
        </div>
    </div>
</template>

<script>
import AlertComponent from './AlertComponent.vue';

export default {
    data: () => {
        return {
            seats: 0,
            alert: {
                show: false,
                success: false,
                message: '',
            },
        };
    },
    props: ['show'],
    methods: {
        hideAlert() {
            this.alert.show = false;
        },
        bookShow() {
            this.$router.push(`/booking/${this.show.id}`);
        }
    },
    async mounted() {
        console.log(this.show);
        const seatsResponse = await fetch(`http://127.0.0.1:8081/api/booking/${this.show.id}`, {
            headers: {
                'access-token': localStorage.getItem("token")
            }
        });
        if (seatsResponse.status === 200) {
            const availableSeats = await seatsResponse.json();
            this.seats = this.show.available_seats - availableSeats.data;
        }
        else {
            this.alert.show = true;
            this.alert.success = false;
            this.alert.message = await seatsResponse.json().message;
        }
    },
    components: { AlertComponent }
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

.show-card-admin-footer>button {
    border-radius: 10px;
}
</style>
