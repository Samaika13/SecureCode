import axios from "axios";

const api = axios.create({
    baseURL: "https://securecode.onrender.com/"
});

export default api;