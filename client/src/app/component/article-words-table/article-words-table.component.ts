import {Component, Input, OnInit} from '@angular/core';
import {
  MatCell, MatCellDef,
  MatColumnDef,
  MatHeaderCell, MatHeaderCellDef,
  MatHeaderRow,
  MatHeaderRowDef,
  MatRow,
  MatRowDef,
  MatTable
} from "@angular/material/table";
import {NormalForm} from "../../model/NormalForm";
import {ArticleServiceService} from '../../service/article-service.service';

@Component({
    selector: 'app-article-words-table',
  imports: [
    MatTable,
    MatColumnDef,
    MatHeaderCell,
    MatCell,
    MatHeaderRow,
    MatRow,
    MatRowDef,
    MatHeaderRowDef,
    MatCellDef,
    MatHeaderCellDef
  ],
    templateUrl: './article-words-table.component.html',
    standalone: true,
    styleUrl: './article-words-table.component.css'
})
export class ArticleWordsTableComponent implements OnInit{
    @Input() data: any;
    dataSource!: NormalForm[];
    displayedColumns: string[] = ['normalForm', 'amount'];

    constructor(
      private service: ArticleServiceService
    ) {
    }

    ngOnInit(): void {
      this.service.getWords(this.data)
        .subscribe(
          response => {
            this.dataSource = response.data
          }
        )
    }

}
