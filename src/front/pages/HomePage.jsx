import React, { useEffect } from "react"
import rigoImageUrl from "../assets/img/rigo-baby.jpg";
import useGlobalReducer from "../hooks/useGlobalReducer.jsx";
import trabajandoImageUrl from "../imagenes/trabajando.jpg";
import { Link } from "react-router-dom";

export const HomePage = () => {

    const { store, dispatch } = useGlobalReducer()

    useEffect(() => {
    }, [])

    return (
        <>
        <div className="text-center mt-5">
            <h1 className="display-4">Bienvenido a tu Pagina de Reservas</h1>
            <p className="lead">Aqui podras registrarte, iniciar sesion y reservar tu espacio en el gimnasio</p>
            <img className="w-25 rounded-circle p-4" src={trabajandoImageUrl}/>
            <h2>Desarrollando Tu Proxima APP</h2>
        </div>

        <div className="d-flex justify-content-center mt-3">
            <Link to="/signup">
            <button className="btn btn-primary" >Sing Up User</button>
            </Link>
            <Link to="/signup/admin">
            <button className="btn btn-primary ms-2">Sing Up Admin</button>
            </Link>
            <Link to="/login">
            <button className="btn btn-primary ms-2">login</button>
            </Link>
        </div>
        </>
    );
}; 