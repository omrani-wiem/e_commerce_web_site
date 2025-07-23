import React from 'react'
import 'bostrap/dist/css/boostrap.min.css'
class HeaderComponent extends Component{
    constructor(props){
        super(props)

        this.state = {

        }
    }

    render(){
        return(
            <div>
                <header>
                    <nav className = "navbar navbar-dark"
                    bg-primary>
                        <div>
                            <a href='/users'></a>
                            user Mangement App
                        </div>
                    </nav>
                </header>
            </div>
        )
    }
}
    