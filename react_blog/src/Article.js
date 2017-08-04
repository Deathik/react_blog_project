import React from 'react';
import { render } from 'react-dom';
import moment from 'moment';
import axios from 'axios';

export default class Article extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            post: this.props.post,
            editing: false
        }
    }

    handleClick() {
        this.setState({
            editing: true
        })
    }

    handleChange(e) {
        e.preventDefault();
        this.setState({
            post: Object.assign({}, this.state.post, {title: this.refs.title.value, text:this.refs.text.value})
        })
    }

    toggleOffEdit(e) {
        e.preventDefault();
        if (!this.state.editing){
            return
        }
        axios({
            url: "/api/posts/" + this.state.post.id + "/",
            method: "put",
            data: { 
                title: this.state.post.title,
                text: this.state.post.text
            },
            xsrfCookieName: 'csrftoken',
            xsrfHeaderName: "X-CSRFToken",
        }).then( response => {console.log(response)});
        this.setState({
            editing: false
        });
    }

    render() {
        const post = this.state.post
        return (
            <article className="col-md-8 col-md-offset-2">
                <div className="thumbnail">
                    <div className='caption'>
                        { !this.state.editing ? <h1 onClick={this.handleClick.bind(this)}>{post.title}</h1> : <input ref="title" value={post.title} onChange={this.handleChange.bind(this)}/>}
                        <h6 style={{color: '#b2b1b1'}}>{ moment(post.last_modified).format('DD MMMM YYYY') }</h6>
                        <p onClick={this.handleClick.bind(this)} style={{ whiteSpace: 'pre-line'}}> {!this.state.editing ? post.text : <textarea ref="text" onChange={this.handleChange.bind(this)} style={{width: "100%", minHeight: 200}} value={post.text}></textarea> }</p>
                        <a className="btn btn-default" href={"/post/" + post.id}>Read more</a>
                        {this.props.username === this.props.post.author && this.state.editing &&
                        <div className="pull-right">
                            <a className="btn btn-info" onClick={this.toggleOffEdit.bind(this)}>
                                <i className="fa fa-floppy-o" aria-hidden="true"></i>
                                <span className="hidden-xs"> Edit Post</span>
                            </a>
                        </div>}
                    </div>
                </div>
            </article>
        )   
    }
}