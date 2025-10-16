import React, { useEffect } from "react"
import rigoImageUrl from "../assets/img/rigo-baby.jpg";
import useGlobalReducer from "../hooks/useGlobalReducer.jsx";
import { Link } from "react-router-dom";

export const AdminPrivate = () => {

    const { store, dispatch } = useGlobalReducer()

    useEffect(() => {
    }, [])

    return (
        <div className="d-flex justify-content-center mt-5">
            <h1>Zona Privada Administrador</h1>
                <Link to="/">
                <button type="back" className="btn btn-primary ms-5">Back</button>
                </Link>
        </div>
    );
}; 