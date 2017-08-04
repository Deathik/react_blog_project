import React from 'react';
import { render } from 'react-dom';
import axios from 'axios';

import InfiniteScroll from 'react-infinite-scroll-component';
import Article from './Article';

class App extends React.Component{
    constructor() {
        super();
        this.state = {
            posts: [],
            page: 2,
            morePosts: true,
            username: document.querySelector('li p.navbar-text').innerHTML,
        };
    }

    componentWillMount() {
            axios.get('/api/posts')
            .then( response => {
                this.setState({posts: response.data.results})
            });
    }

    getData() {
        if (this.state.morePosts){
            axios.get('/api/posts/?page=' + this.state.page)
            .then(response => {
                this.setState({
                    page: this.state.page + 1,
                    posts: [...this.state.posts, ...response.data.results]
                });
                if(response.data.next === null){
                    this.setState({morePosts: false});
                }
            })
        }
    }

    render(){
        let loading = <div className="col-md-8 col-md-offset-2 text-center">
            Loading...</div>;
        return (
            <div className="container">
                <div className="row">
                    <InfiniteScroll
                        next={this.getData.bind(this)}
                        hasMore={this.state.morePosts}
                        loader={loading} 
                    >
                    { this.state.posts.map( (item, i) => {
                        return <Article post={item} key={i} username={this.state.username} />
                    })}
                    </InfiniteScroll>
                </div>  
            </div>
        )
    }
}

render(<App />, document.getElementById('root'));