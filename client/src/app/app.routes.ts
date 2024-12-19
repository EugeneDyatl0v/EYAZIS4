import { Routes } from '@angular/router';
import {ArticleComponent} from "./component/article/article.component";
import {AddingArticleComponent} from "./component/adding-article/adding-article.component";

export const routes: Routes = [
    {
        path: 'articles/:id',
        component: ArticleComponent
    },
    {
        path: 'articles',
        component: AddingArticleComponent
    }
];
