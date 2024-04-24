package com.example.application.data;

import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

import com.github.javafaker.Faker;

@Component
public class DatabaseLoader implements CommandLineRunner {

    private final SamplePersonRepository repository;
    private final Faker faker;

    public DatabaseLoader(SamplePersonRepository repository) {
        this.repository = repository;
        this.faker = new Faker();
    }

    @Override
    public void run(String... strings) throws Exception {
    	 for (int i = 0; i < 100; i++) {
             String firstName = faker.name().firstName();
             String lastName = faker.name().lastName();
             String dob = faker.date().birthday().toString();
             String phone=faker.phoneNumber().toString();
             String occupation=faker.job().toString();
             
             SamplePerson person = new SamplePerson();
             person.setDateOfBirth(null);
             person.setEmail("test@test.com");
             person.setFirstName(firstName);
             person.setLastName(lastName);
             person.setOccupation(occupation);
             person.setPhone(phone);
             person.setRole(occupation);
             repository.save(person);
         }
 
    }
}
