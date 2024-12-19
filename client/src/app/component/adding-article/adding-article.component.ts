import { Component } from '@angular/core';
import {FormBuilder, FormGroup, ReactiveFormsModule, Validators} from "@angular/forms";
import {MatFormField} from "@angular/material/form-field";
import { MatFormFieldModule } from '@angular/material/form-field';
import {MatInput} from "@angular/material/input";
import {NgIf} from "@angular/common";
import {MatCheckbox} from "@angular/material/checkbox";
import {MatButton} from "@angular/material/button";
import {ArticleServiceService} from "../../service/article-service.service";
import {Article} from "../../model/Article";

@Component({
    selector: 'app-adding-article',
    imports: [
        ReactiveFormsModule,
        MatFormFieldModule,
        MatFormField,
        MatInput,
        NgIf,
        MatCheckbox,
        MatButton
    ],
    templateUrl: './adding-article.component.html',
    standalone: true,
    styleUrl: './adding-article.component.css'
})
export class AddingArticleComponent {
    articleForm: FormGroup;

    constructor(
        private fb: FormBuilder,
        private service: ArticleServiceService
    ) {
        this.articleForm = this.fb.group({
            title: ['', [Validators.required]],
            text: ['', [Validators.required]],
            source_language: ['', [Validators.required]],
        });

        // Dynamically validate 'original_article_id' based on 'is_original'
        this.articleForm.get('is_original')?.valueChanges.subscribe((isOriginal) => {
            if (!isOriginal) {
                this.articleForm.get('original_article_id')?.setValidators([Validators.required]);
            } else {
                this.articleForm.get('original_article_id')?.clearValidators();
            }
            this.articleForm.get('original_article_id')?.updateValueAndValidity();
        });
    }

    onSubmit() {
        if (this.articleForm.valid) {
            let article: Article = {
                title: this.articleForm.get("title")?.value || '',
                text: this.articleForm.get("text")?.value || '',
                source_language: this.articleForm.get("source_language")?.value || 'ru',
                is_original: true,
                original_article_id: null
            }
            console.log(article);
            this.service.createArticle(article).subscribe(
                response => {
                    console.log("success");
                    console.log(response);
                    window.location.href = `/articles/${response.data.id}`;
                }
            )
        }
    }
}
