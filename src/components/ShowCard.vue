<template>
    <div class="containerS">
        <div class="show-card-admin">
            <h2>{{ show.name }}</h2>
            <div class="venue-card-admin-footer">
                <button @click="bookShow">Book Show</button>
            </div>
        </div>
    </div>
</template>

<script>


export default {
    data: () => {
        return {
        }
    },
    props: ['show'],
    methods: {
        bookShow() {
            this.$router.push(`/booking/${this.show.id}`)
        }
    },
    mounted() {

    }
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
