import { Routes } from '@angular/router';
import {ArticleComponent} from "./component/article/article.component";

export const routes: Routes = [
    {
        path: 'articles/:id',
        component: ArticleComponent
    }
];
