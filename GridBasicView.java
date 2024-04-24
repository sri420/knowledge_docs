package com.example.application.views.personform;

import com.example.application.data.PagingDataProvider;
import com.example.application.data.SamplePerson;
import com.example.application.data.SamplePersonRepository;
import com.example.application.services.SamplePersonService;
import com.example.application.views.MainLayout;
import com.vaadin.flow.component.button.Button;
import com.vaadin.flow.component.dependency.Uses;
import com.vaadin.flow.component.grid.Grid;
import com.vaadin.flow.component.icon.Icon;
import com.vaadin.flow.component.orderedlayout.VerticalLayout;
import com.vaadin.flow.router.PageTitle;
import com.vaadin.flow.router.Route;

@PageTitle("Grid")
@Route(value = "grid", layout = MainLayout.class)
@Uses(Icon.class)
public class GridBasicView extends VerticalLayout {
	
	
	SamplePersonRepository samplePersonRepository;

	 public GridBasicView(SamplePersonRepository samplePersonRepository) {
		
		 
		 PagingDataProvider dataProvider = new PagingDataProvider(samplePersonRepository);
		 Grid<SamplePerson> grid = new Grid<>(SamplePerson.class);
		 grid.setDataProvider(dataProvider);
		 grid.setPageSize(5);

		 Button firstPageButton = new Button("First", event -> dataProvider.firstPage());
		 Button previousPageButton = new Button("Previous", event -> dataProvider.previousPage());
		 Button nextPageButton = new Button("Next", event -> dataProvider.nextPage());
		 Button lastPageButton = new Button("Last", event -> dataProvider.lastPage());

		 add(firstPageButton, previousPageButton, nextPageButton, lastPageButton, grid);
		 //
		 
		 
	 }
	
}
