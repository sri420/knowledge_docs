package com.example.application.data;

import java.util.List;
import java.util.stream.Stream;

import org.springframework.data.domain.PageRequest;

import com.vaadin.flow.data.provider.AbstractBackEndDataProvider;
import com.vaadin.flow.data.provider.Query;

public class PagingDataProvider extends AbstractBackEndDataProvider<SamplePerson, Void> {
    private SamplePersonRepository repository;
    private int currentPage = 0;
    private static final int PAGE_SIZE = 5;
    // constructor and other methods...

    public PagingDataProvider(SamplePersonRepository samplePersonRepository) {
		this.repository=samplePersonRepository;
	}

	public void nextPage() {
        currentPage++;
        refreshAll();
    }

    public void previousPage() {
        currentPage = Math.max(0, currentPage - 1);
        refreshAll();
    }

    public void firstPage() {
        currentPage = 0;
        refreshAll();
    }

    public void lastPage() {
    	 long count = repository.count();
         currentPage = (int) (count / PAGE_SIZE);
         if (count % PAGE_SIZE == 0) {
             currentPage--;
         }
         refreshAll();
        refreshAll();
    }

    public int getPageSize() {
        return PAGE_SIZE;
    }
	

	@Override
	protected int sizeInBackEnd(Query<SamplePerson, Void> query) {
		return (int) repository.count();
		
	}

	@Override
	protected Stream<SamplePerson> fetchFromBackEnd(Query<SamplePerson, Void> query) {
		  int offset = query.getOffset();
		    int limit = query.getLimit();

		    // Fetch the required page of data from your repository
		    List<SamplePerson> pageOfData = repository.findAll(PageRequest.of(offset / limit, limit)).getContent();

		    return pageOfData.stream();
	}

}
