import {Component, Input} from '@angular/core';
import {MatCard, MatCardHeader, MatCardModule} from "@angular/material/card";

@Component({
    selector: 'app-article-text',
    imports: [
        MatCard,
        MatCardModule,
        MatCardHeader
    ],
    templateUrl: './article-text.component.html',
    standalone: true,
    styleUrl: './article-text.component.css'
})
export class ArticleTextComponent {
    @Input() data: any;
}
